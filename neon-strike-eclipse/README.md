# Neon Strike: Eclipse Protocol — v8 FIRST CONTACT

Linha atual de desenvolvimento do shooter single-file. Os checkpoints anteriores e o `combatgalaxies.html` histórico permanecem preservados.

## Base canônica

- Jogo: `neon_strike_eclipse_protocol_v8_first_contact.html`
- SHA-256: `1e757b4046d00cd8454b951782577fbe1a0eaff66e4d53a7d15a9dabbf34d5d5`.
- Arquivo único, sem CDN, imports ou assets externos.
- Save: `neon_strike_eclipse_v8`, migrando v7/v6/v5/v4/v3/v2.

## Gancho

> Você não mata o chefe. Você o desmonta e veste as peças.

A v8 preserva 2 prismas do Arconte, 3 casulos da Tecelã, 2 canhões do Leviatã, 14 fusões comportamentais, 3 atos, 6 posturas de chefe e as 4 doutrinas de arma da v7.

## v8 — Assimilação de Doutrina

A primeira peça roubada já modifica a arma-base, sem depender da sorte das cartas:

- **Striker → Ressonância Rail** — ecos perfurantes na quinta rajada.
- **Aegis → Reversor Aegis** — baterias de cobertura e contra-fogo na sexta rajada.
- **Phantom → Eco Fantasma** — agulhas rápidas e teleguiadas na quarta rajada.
- **Revenant → Mandíbula Parasita** — estilhaços curtos nas rajadas alternadas.

## Primeiros 60 segundos

Na mesma seed de QA:

| Núcleo | 1ª evolução | 1º chefe | Assimilação |
|---|---:|---:|---:|
| Striker | 8.75 s | 26.00 s | 30.75 s |
| Aegis | 7.75 s | 25.50 s | 33.00 s |
| Phantom | 4.25 s | 17.25 s | 21.00 s |
| Revenant | 6.25 s | 26.25 s | 29.75 s |

O gancho aparece no primeiro minuto em **4/4 núcleos**.

## QA v8

- Stress 3 chefes × 3 fases: pico 52 projéteis hostis.
- Robô 300 s: 3/3 chefes em touch, desktop retrato e desktop paisagem.
- Picos hostis: 77 / 178 / 292, todos sob hard cap 200/330.
- Heap touch 300→600 s: +48,916 bytes (~0.05 MB).
- `node --check`: PASS.
- Erros não tratados nas baterias finais: 0.

Relatório completo: `QA_REPORT_v8_20260905.md`.
Régua: `REGUA_STATUS_v8.md`.

## Google Drive

Pasta do projeto:
https://drive.google.com/drive/folders/14JSsgfglD3oEIyzK8eKm6v5ibFJuL8h9

HTML v8:
https://drive.google.com/file/d/1rlyQHu32hC8Q03xjxN2YgBw9zYAgzEIY/view?usp=drivesdk

Contact sheet das assimilações:
https://drive.google.com/file/d/1RygWAtQDamSxf9VpJFOFJzAjLGLxSmIg/view?usp=drivesdk

## Próximo alvo

Expandir escopo somente por conteúdo que reforce o gancho: novos chefes precisam ter partes desmontáveis e decisões de alvo próprias. Nada de chefe antigo com mais HP e mais projéteis.
