from __future__ import annotations

import json
import shutil
import subprocess
import wave
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import sherpa_onnx
import soundfile as sf

BASE = Path(__file__).resolve().parent
MODELS = BASE / "modelos"
OUT = BASE / "saida"
TEMP = BASE / "temporarios"
TEXT_FILE = BASE / "narracao_corrigida.txt"


@dataclass(frozen=True)
class VoiceSpec:
    label: str
    folder: str
    model: str
    speed: float
    pause_seconds: float
    description: str


VOICES = [
    VoiceSpec(
        label="faber",
        folder="vits-piper-pt_BR-faber-medium",
        model="pt_BR-faber-medium.onnx",
        speed=1.08,
        pause_seconds=0.45,
        description="Dicção mais limpa — recomendada",
    ),
    VoiceSpec(
        label="miro",
        folder="vits-piper-pt_BR-miro-high",
        model="pt_BR-miro-high.onnx",
        speed=1.00,
        pause_seconds=0.50,
        description="Timbre mais grave e pausado",
    ),
    VoiceSpec(
        label="dii",
        folder="vits-piper-pt_BR-dii-high",
        model="pt_BR-dii-high.onnx",
        speed=0.98,
        pause_seconds=0.48,
        description="Timbre mais suave",
    ),
]


def run(cmd: list[str]) -> None:
    print("+", " ".join(cmd), flush=True)
    subprocess.run(cmd, check=True)


def srt_time(seconds: float) -> str:
    milliseconds = max(0, int(round(seconds * 1000)))
    hours, milliseconds = divmod(milliseconds, 3_600_000)
    minutes, milliseconds = divmod(milliseconds, 60_000)
    secs, milliseconds = divmod(milliseconds, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{milliseconds:03d}"


def load_tts(spec: VoiceSpec) -> sherpa_onnx.OfflineTts:
    folder = MODELS / spec.folder
    config = sherpa_onnx.OfflineTtsConfig(
        model=sherpa_onnx.OfflineTtsModelConfig(
            vits=sherpa_onnx.OfflineTtsVitsModelConfig(
                model=str(folder / spec.model),
                tokens=str(folder / "tokens.txt"),
                data_dir=str(folder / "espeak-ng-data"),
            ),
            num_threads=2,
            debug=False,
            provider="cpu",
        ),
        max_num_sentences=1,
    )
    if not config.validate():
        raise RuntimeError(f"Configuração inválida para {spec.label}: {folder}")
    return sherpa_onnx.OfflineTts(config)


def render_voice(spec: VoiceSpec, paragraphs: list[str]) -> dict[str, object]:
    print(f"\n=== Gerando voz {spec.label} ===", flush=True)
    tts = load_tts(spec)
    all_samples: list[np.ndarray] = []
    subtitle_rows: list[tuple[float, float, str]] = []
    cursor = 0.0
    sample_rate: int | None = None

    voice_temp = TEMP / spec.label
    voice_temp.mkdir(parents=True, exist_ok=True)

    for index, paragraph in enumerate(paragraphs, start=1):
        print(f"[{spec.label}] trecho {index}/{len(paragraphs)}", flush=True)
        audio = tts.generate(text=paragraph, sid=0, speed=spec.speed)
        samples = np.asarray(audio.samples, dtype=np.float32)
        if samples.ndim != 1:
            samples = samples.reshape(-1)
        if sample_rate is None:
            sample_rate = int(audio.sample_rate)
        elif sample_rate != int(audio.sample_rate):
            raise RuntimeError("Taxa de amostragem mudou durante a geração")

        duration = len(samples) / sample_rate
        start = cursor
        end = cursor + duration
        subtitle_rows.append((start, end, paragraph))
        all_samples.append(samples)
        cursor = end

        sf.write(voice_temp / f"trecho_{index:02d}.wav", samples, sample_rate, subtype="PCM_16")

        if index < len(paragraphs):
            silence = np.zeros(int(round(sample_rate * spec.pause_seconds)), dtype=np.float32)
            all_samples.append(silence)
            cursor += spec.pause_seconds

    if sample_rate is None:
        raise RuntimeError("Nenhum áudio foi produzido")

    raw = np.concatenate(all_samples)
    raw_wav = OUT / f"NARRACAO_18_LEILAO_{spec.label.upper()}_SEM_TRATAMENTO.wav"
    processed_wav = OUT / f"NARRACAO_18_LEILAO_{spec.label.upper()}.wav"
    mp3 = OUT / f"NARRACAO_18_LEILAO_{spec.label.upper()}.mp3"
    srt = OUT / f"NARRACAO_18_LEILAO_{spec.label.upper()}.srt"

    sf.write(raw_wav, raw, sample_rate, subtype="PCM_16")

    filters = (
        "highpass=f=55,"
        "lowpass=f=12000,"
        "bass=g=2.5:f=120:w=0.6,"
        "acompressor=threshold=0.12:ratio=2.5:attack=20:release=180:makeup=1.45,"
        "loudnorm=I=-16:TP=-1.5:LRA=7"
    )

    run([
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "warning",
        "-i", str(raw_wav), "-af", filters,
        "-ar", "44100", "-ac", "1", "-c:a", "pcm_s16le", str(processed_wav),
    ])
    run([
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "warning",
        "-i", str(processed_wav), "-c:a", "libmp3lame", "-b:a", "192k", str(mp3),
    ])

    srt_lines: list[str] = []
    for number, (start, end, paragraph) in enumerate(subtitle_rows, start=1):
        srt_lines.extend([
            str(number),
            f"{srt_time(start)} --> {srt_time(end)}",
            paragraph,
            "",
        ])
    srt.write_text("\n".join(srt_lines), encoding="utf-8")

    duration_raw = len(raw) / sample_rate
    return {
        "voz": spec.label,
        "descricao": spec.description,
        "modelo": spec.model,
        "sample_rate_modelo": sample_rate,
        "velocidade": spec.speed,
        "pausa_entre_paragrafos": spec.pause_seconds,
        "duracao_segundos": round(duration_raw, 3),
        "mp3": mp3.name,
        "wav": processed_wav.name,
        "wav_sem_tratamento": raw_wav.name,
        "srt": srt.name,
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    TEMP.mkdir(parents=True, exist_ok=True)

    text = TEXT_FILE.read_text(encoding="utf-8-sig").strip()
    paragraphs = [p.strip().replace("\n", " ") for p in text.split("\n\n") if p.strip()]
    if not paragraphs:
        raise RuntimeError("Texto de narração vazio")

    reports = [render_voice(spec, paragraphs) for spec in VOICES]

    shutil.copy2(OUT / "NARRACAO_18_LEILAO_FABER.mp3", OUT / "NARRACAO_18_LEILAO_RECOMENDADA.mp3")
    shutil.copy2(OUT / "NARRACAO_18_LEILAO_FABER.srt", OUT / "NARRACAO_18_LEILAO_RECOMENDADA.srt")

    report_json = OUT / "RELATORIO_TECNICO.json"
    report_json.write_text(json.dumps({"vozes": reports}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    report_md = OUT / "RELATORIO.md"
    lines = [
        "# Relatório da narração Piper/Sherpa",
        "",
        "Texto revisado com acentuação correta e modelos brasileiros de 22.050 Hz.",
        "Tratamento final: filtro de graves leve, compressor e normalização em -16 LUFS.",
        "",
        "## Arquivos gerados",
        "",
    ]
    for item in reports:
        lines.extend([
            f"### {str(item['voz']).upper()} — {item['descricao']}",
            f"- Duração: {item['duracao_segundos']} s",
            f"- Modelo: {item['modelo']}",
            f"- MP3: `{item['mp3']}`",
            f"- WAV tratado: `{item['wav']}`",
            f"- WAV sem tratamento: `{item['wav_sem_tratamento']}`",
            f"- Legenda: `{item['srt']}`",
            "",
        ])
    lines.extend([
        "## Recomendação inicial",
        "",
        "A voz **faber** foi definida como recomendada por apresentar dicção mais limpa.",
    ])
    report_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("\nArquivos finais:")
    for path in sorted(OUT.iterdir()):
        print(f"- {path.name} ({path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
