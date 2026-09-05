# Neon Strike: Eclipse Protocol — v6 THREE ACTS

Linha atual de desenvolvimento do shooter single-file. Os checkpoints v4/v5 e o `combatgalaxies.html` histórico permanecem preservados.

## Base canônica

- Jogo: `neon_strike_eclipse_protocol_v6_three_acts.html`
- Tamanho: 222.344 bytes.
- SHA-256: `bdb086f41513b212748865fbd73c8778b297f55a551e290a5b2c4bd3f944f8fa`.
- Arquivo único, sem CDN, imports ou assets externos.
- Save: `neon_strike_eclipse_v6`, migrando v5/v4/v3/v2.

## Gancho preservado

> Você não mata o chefe. Você o desmonta e veste as peças.

A v6 preserva 2 prismas do Arconte, 3 casulos da Tecelã, 2 canhões do Leviatã, 14 fusões comportamentais e 35 opções totais de construção/fusão.

## v6 — três atos + postura de chefe

- Ato I: **Corredor de Íons** — trilhos convergentes e portais laterais.
- Ato II: **Campo de Fratura** — placas fraturadas em deriva.
- Ato III: **Forja do Eclipse** — monólitos laterais e arcos de máquina.
- cenário usa família `ENV` neutra dessaturada, sem roubar rosa/âmbar/ciano/menta da gameplay;
- seis posturas de intenção antes do ataque: `fan`, `radial`, `laser`, `field`, `ram`, `summon`;
- intenção letal usa rosa; `summon` é não letal e usa ENV neutro;
- telegraph de intenção: 0,72 s; arming de projétil: 0,60 s;
- mina, sniper e telegrafos auxiliares tiveram exceções antigas de paleta corrigidas;
- hard cap absoluto: 200 projéteis touch / 330 desktop.

## QA v6

- `node --check`: PASS;
- 14/14 fusões ainda ativáveis;
- stress dirigido: pico 52 touch / 52 desktop; cores hostis somente `#ff2f6e` e `#ff5c8a`;
- robô 300 s: 3/3 chefes em touch portrait, desktop portrait e landscape;
- picos do robô: 127 / 174 / 329, todos dentro da régua;
- heap touch 300→600 s após GC: +76.112 bytes na medição final;
- erros não tratados nas baterias finais: 0.

Pendências externas: Android físico 10 min, avaliação humana de áudio/impacto e baseline histórica aprovada para screenshot regression.

## Google Drive

Pasta do projeto:
https://drive.google.com/drive/folders/14JSsgfglD3oEIyzK8eKm6v5ibFJuL8h9

HTML v6:
https://drive.google.com/file/d/1nL6e4kf9DFMOJ_RYtVhgkLi-c9ddRBLf/view?usp=drivesdk

ZIP v6:
https://drive.google.com/file/d/1TfIof9inPcWKUoRMiAuAoeIf8VeCja9f/view?usp=drivesdk

Régua v4:
https://drive.google.com/file/d/1_LCPO0enNBbps-c0hgEm6Mu4wEgi1sA_/view?usp=drivesdk

QA v6:
https://drive.google.com/file/d/1ULHBJBOMl44ycfZf424xlrflnCrjqhqV/view?usp=drivesdk

Contact sheet das posturas:
https://drive.google.com/file/d/1UDZmGpUdWKeHsf_2x3snqtOlfSm2hZjW/view?usp=drivesdk

## Próxima auditoria

Não inflar conteúdo. O crítico deve agora procurar a menor dimensão restante entre sensação de tiro/áudio, distinção real dos quatro núcleos e primeiros 60 segundos.