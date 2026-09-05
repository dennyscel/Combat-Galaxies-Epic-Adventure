# Neon Strike: Eclipse Protocol — v7 CORE DOCTRINES

Linha atual de desenvolvimento do shooter single-file. Os checkpoints v4/v5/v6 e o `combatgalaxies.html` histórico permanecem preservados.

## Base canônica

- Jogo: `neon_strike_eclipse_protocol_v7_core_doctrines.html`
- Tamanho: 225.484 bytes.
- SHA-256: `42cc514a5b7841659305f18cf44acd45cf3da06bf6db85126a90779656c7e742`.
- Arquivo único, sem CDN, imports ou assets externos.
- Save: `neon_strike_eclipse_v7`, migrando v6/v5/v4/v3/v2.

## Gancho preservado

> Você não mata o chefe. Você o desmonta e veste as peças.

A v7 preserva os três atos, seis posturas de chefe, 2 prismas do Arconte, 3 casulos da Tecelã, 2 canhões do Leviatã, 14 fusões comportamentais e 35 opções totais de construção/fusão.

## v7 — quatro doutrinas de arma

- **Striker — Lança de Pulso:** linha/rail de alta velocidade, com disparo pesado periódico.
- **Aegis — Bateria Gêmea:** cobertura larga, duas baterias e salvas laterais; combina com a doutrina defensiva.
- **Phantom — Agulha Espectral:** poucos projéteis muito rápidos, estreitos, teleguiados e perfurantes.
- **Revenant — Mandíbula de Ruptura:** escopeta larga, projéteis grandes e de vida curta; exige aproximação.

Cada núcleo também tem assinatura sonora própria. As peças roubadas e fusões entram por cima da doutrina, então o gancho continua sendo o centro da build.

## QA v7

`coreProbe()` mediu 12 rajadas sem perks/peças:

| Núcleo | Projéteis | Abertura | Velocidade média | Raio | Vida | Perfuração média |
|---|---:|---:|---:|---:|---:|---:|
| Striker | 14 | 0,00 | 1143 | 4,80 | 2,51 s | 0,14 |
| Aegis | 28 | 0,76 rad | 894 | 4,57 | 2,64 s | 0,00 |
| Phantom | 15 | 0,00 | 1424 | 3,72 | 2,12 s | 1,60 |
| Revenant | 40 | 0,41 rad | 756 | 6,03 | 0,84 s | 0,10 |

Na mesma seed de 300 s, **4/4 núcleos cobriram 3/3 chefes**, com picos hostis de 98/178/142/176 — todos abaixo do hard cap touch de 200.

Heap touch: 2.847.760 bytes aos 300 s → 2.842.924 aos 600 s; 0 exceções, setor 29. `node --check`: PASS.

## Google Drive

Pasta do projeto:
https://drive.google.com/drive/folders/14JSsgfglD3oEIyzK8eKm6v5ibFJuL8h9

HTML v7:
https://drive.google.com/file/d/1NTNnobx8PQbzHEIqkiKMzXlE9bCo3o3Z/view?usp=drivesdk

ZIP v7:
https://drive.google.com/file/d/15EpdyOJaGrbPjge6iVChy5AkIis3uYJy/view?usp=drivesdk

Régua v5:
https://drive.google.com/file/d/1uiveqsQQr7FF2ZJIYunHXl4Yybp0Ysks/view?usp=drivesdk

QA v7:
https://drive.google.com/file/d/1eNIlBfhe5pY0c3qU7201jExJfrRJwOCE/view?usp=drivesdk

Contact sheet das doutrinas:
https://drive.google.com/file/d/1y4AAr0lJUQNCKJS5CWtFNf9wsSdJ9Yku/view?usp=drivesdk

## Próximo alvo

Medir e melhorar os **primeiros 60 segundos**. Não adicionar conteúdo genérico antes de provar essa janela.