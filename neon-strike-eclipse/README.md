# Neon Strike: Eclipse Protocol — v4 GAUNTLET

Nova linha de desenvolvimento do shooter single-file, preservando o Combat Galaxies histórico deste repositório.

## Base atual

- Jogo: `neon_strike_eclipse_protocol_v4_gauntlet.html`
- Tamanho: 205388 bytes
- SHA-256: `4fcc24a35c84a444a970c350571c18157f56bd60fe1bc46259bd30d6db7d8ac2`
- Arquivo único, sem CDN, sem assets externos, sem build.

## Gancho central

> Você não mata o chefe. Você o desmonta e veste as peças.

A v4 fecha esse gancho no código executável:

- Arconte: 2 prismas destrutíveis → `prism`.
- Tecelã: 3 casulos destrutíveis → `pod`.
- Leviatã: 2 torres destrutíveis → `cannon`.
- Matar o chefe antes destrói as partes restantes sem loot.
- As peças coletadas mudam a silhueta e o comportamento da nave.

## Profundidade nova

Cinco fusões comportamentais foram adicionadas: Leque Rail, Tempestade Crítica, Matilha Vetorial, Coroa Sentinela e Corte de Fase. Os quatro núcleos também passam a ter assinatura de tiro/silhueta distinta.

## Justiça e leitura

- projéteis hostis forçados à rampa rosa de ameaça;
- arming visual/mecânico de 0,60 s;
- postura/telegraph de chefe de 0,68 s;
- primeiro chefe antecipado para o setor 3;
- PRNG de gameplay separado do RNG visual;
- seed repetível por `?seed=<n>`;
- API de QA disponível apenas com `?qa=1`.

## QA executado em 2026-09-05

- `node --check`: PASS
- Chromium headless 390×844: 0 erros
- Chromium headless 1280×720: 0 erros
- gancho 3/3 chefes: PASS
- rush no núcleo sem loot: PASS
- stress touch 3 chefes × 3 fases: pico observado 57 projéteis
- cores hostis observadas: apenas `#ff2f6e` e `#ff5c8a`

Ainda falta validar 60 fps/heap por sessão longa em Android físico e construir comparação visual automática entre versões.

## Google Drive — fonte e pacote completo

Pasta do projeto:
https://drive.google.com/drive/folders/14JSsgfglD3oEIyzK8eKm6v5ibFJuL8h9

HTML:
https://drive.google.com/file/d/19XV5MIQOYqEcORVwPvNaAYh4NFMFgRnW/view?usp=drivesdk

ZIP completo:
https://drive.google.com/file/d/1QYkbsCTs55pkHmVDUNshFUG0Q7szSfmf/view?usp=drivesdk

Régua v2:
https://drive.google.com/file/d/14Jm1aU9L3I3Yg263_WipDSgwBXKZ2SJ-/view?usp=drivesdk

Relatório QA:
https://drive.google.com/file/d/1rHo2_fca58yT4a8jUX6c5I45ZpyFCcTu/view?usp=drivesdk

## Próximo alvo

Não inflar conteúdo genérico. A próxima iteração deve atacar a menor nota da régua: ampliar fusões que mudam comportamento, depois validar hardware Android e comparação visual automática.
