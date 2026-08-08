from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import numpy as np
import sherpa_onnx
import soundfile as sf

BASE = Path(__file__).resolve().parent
MODELS = BASE / "modelos"
OUT = BASE / "saida"
SEG = OUT / "segmentos"
TMP = BASE / "temporarios"

MODEL_DIR = MODELS / "vits-piper-pt_BR-faber-medium"
MODEL_FILE = MODEL_DIR / "pt_BR-faber-medium.onnx"
SPEED = 1.08


def run(cmd: list[str]) -> None:
    print("+", " ".join(cmd), flush=True)
    subprocess.run(cmd, check=True)


def tts_text(text: str) -> str:
    replacements = {
        "18º": "décimo oitavo",
        "Atari 2600": "Atari dois mil e seiscentos",
        "classicosdosgames.com.br": "clássicos dos games ponto com ponto br",
    }
    for a, b in replacements.items():
        text = text.replace(a, b)
    return text


def load_tts() -> sherpa_onnx.OfflineTts:
    config = sherpa_onnx.OfflineTtsConfig(
        model=sherpa_onnx.OfflineTtsModelConfig(
            vits=sherpa_onnx.OfflineTtsVitsModelConfig(
                model=str(MODEL_FILE),
                tokens=str(MODEL_DIR / "tokens.txt"),
                data_dir=str(MODEL_DIR / "espeak-ng-data"),
            ),
            num_threads=2,
            debug=False,
            provider="cpu",
        ),
        max_num_sentences=1,
    )
    if not config.validate():
        raise RuntimeError("Configuração inválida para Faber Medium")
    return sherpa_onnx.OfflineTts(config)


def process_segment(raw_path: Path, out_path: Path) -> None:
    filters = (
        "highpass=f=70,"
        "lowpass=f=12500,"
        "acompressor=threshold=-18dB:ratio=2.2:attack=15:release=180,"
        "loudnorm=I=-16:TP=-1.5:LRA=8"
    )
    run([
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "warning",
        "-i", str(raw_path),
        "-af", filters,
        "-ar", "48000", "-ac", "1", "-c:a", "pcm_s16le",
        str(out_path),
    ])


def render(script_name: str, label: str, tts: sherpa_onnx.OfflineTts) -> dict:
    text = (BASE / script_name).read_text(encoding="utf-8-sig").strip()
    paragraphs = [p.strip().replace("\n", " ") for p in text.split("\n\n") if p.strip()]
    seg_dir = SEG / label
    raw_dir = TMP / label
    seg_dir.mkdir(parents=True, exist_ok=True)
    raw_dir.mkdir(parents=True, exist_ok=True)

    manifest = []
    for idx, paragraph in enumerate(paragraphs, 1):
        spoken = tts_text(paragraph)
        print(f"[{label}] segmento {idx}/{len(paragraphs)}", flush=True)
        audio = tts.generate(text=spoken, sid=0, speed=SPEED)
        samples = np.asarray(audio.samples, dtype=np.float32).reshape(-1)
        sr = int(audio.sample_rate)
        raw = raw_dir / f"seg_{idx:02d}_raw.wav"
        processed = seg_dir / f"seg_{idx:02d}.wav"
        sf.write(raw, samples, sr, subtype="PCM_16")
        process_segment(raw, processed)
        info = sf.info(processed)
        manifest.append({
            "index": idx,
            "texto_oficial": paragraph,
            "texto_tts": spoken,
            "arquivo": processed.name,
            "duracao": round(info.duration, 3),
            "sample_rate": info.samplerate,
            "channels": info.channels,
        })

    # Referência contínua mono 44,1 kHz, com pausas discretas entre parágrafos.
    concat_parts = []
    for idx in range(1, len(paragraphs) + 1):
        concat_parts.append(seg_dir / f"seg_{idx:02d}.wav")
        if idx < len(paragraphs):
            silence = seg_dir / f"silence_{idx:02d}.wav"
            run([
                "ffmpeg", "-y", "-hide_banner", "-loglevel", "warning",
                "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono",
                "-t", "0.45", "-c:a", "pcm_s16le", str(silence),
            ])
            concat_parts.append(silence)

    concat_file = TMP / f"concat_{label}.txt"
    concat_file.write_text("\n".join(f"file '{p.resolve()}'" for p in concat_parts) + "\n", encoding="utf-8")
    continuous_wav = OUT / f"NARRACAO_{label.upper()}_FABER_CONTINUA_48000_MONO.wav"
    run([
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "warning",
        "-f", "concat", "-safe", "0", "-i", str(concat_file),
        "-c:a", "pcm_s16le", str(continuous_wav),
    ])
    mono_mp3 = OUT / f"NARRACAO_{label.upper()}_FABER_MONO_44100.mp3"
    run([
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "warning",
        "-i", str(continuous_wav), "-ar", "44100", "-ac", "1",
        "-c:a", "libmp3lame", "-b:a", "192k", str(mono_mp3),
    ])
    stereo_mp3 = OUT / f"NARRACAO_{label.upper()}_FABER_STEREO_48000.mp3"
    run([
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "warning",
        "-i", str(continuous_wav),
        "-af", "pan=stereo|c0=c0|c1=c0",
        "-ar", "48000", "-ac", "2",
        "-c:a", "libmp3lame", "-b:a", "192k", str(stereo_mp3),
    ])

    return {
        "label": label,
        "modelo": MODEL_FILE.name,
        "speed": SPEED,
        "segmentos": manifest,
        "narracao_mono_mp3": mono_mp3.name,
        "narracao_stereo_mp3": stereo_mp3.name,
        "narracao_continua_wav": continuous_wav.name,
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    SEG.mkdir(parents=True, exist_ok=True)
    TMP.mkdir(parents=True, exist_ok=True)
    tts = load_tts()
    reports = [
        render("ROTEIRO_TTS_VIDEO_10MIN.txt", "video10", tts),
        render("ROTEIRO_TTS_VIDEO_5MIN.txt", "video5", tts),
    ]
    (OUT / "MANIFESTO_AUDIO.json").write_text(
        json.dumps({"motor": "sherpa_onnx.OfflineTts", "voz": "Faber Medium", "reports": reports}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    shutil.copy2(BASE / "ROTEIRO_TTS_VIDEO_10MIN.txt", OUT / "ROTEIRO_TTS_VIDEO_10MIN.txt")
    shutil.copy2(BASE / "ROTEIRO_TTS_VIDEO_5MIN.txt", OUT / "ROTEIRO_TTS_VIDEO_5MIN.txt")


if __name__ == "__main__":
    main()
