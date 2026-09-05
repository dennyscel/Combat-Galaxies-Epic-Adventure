# Neon Strike: Eclipse Protocol — v9 HARDLINE

Linha atual de desenvolvimento do shooter single-file. Os checkpoints anteriores e o `combatgalaxies.html` histórico permanecem preservados.

## Base candidata para teste humano

- Jogo: `neon_strike_eclipse_protocol_v9_hardline.html`
- SHA-256: `d0022c535b7c98be75e30bc4b28c929ac4c8f1e614f2cb3371399d0717c7d8d0`.
- Arquivo único, sem CDN, imports ou assets externos.
- Save: `neon_strike_eclipse_v9`, migrando v8/v7/v6/v5/v4/v3/v2.

## Gancho preservado

> Você não mata o chefe. Você o desmonta e veste as peças.

A v9 mantém as tecnologias roubadas, 14 fusões, três atos, quatro doutrinas e as quatro assimilações da v8. O foco desta versão é dificuldade e progressão.

## v9 — HARDLINE

### Chefes

- Casco base aproximadamente 2× maior e escala adicional por MK.
- Partes destrutíveis muito mais resistentes.
- Tecelã reduz o dano ao núcleo para 22% enquanto houver casulos.
- Fase 3 começa com 38% do casco restante e recebe armadura adicional.
- Intervalos entre repertórios foram reduzidos, mantendo telegraph de 0,66 s.
- Arrancar uma peça agora provoca uma contramedida específica do chefe.
- Padrões receberam mais salvas e pressão sem ultrapassar o teto técnico de projéteis.

### Progressão

- XP efetiva reduzida para 60%.
- Primeiro nível passa de 65 para 95 XP.
- Curva dos níveis seguintes ficou significativamente mais íngreme.
- Cura entre setores caiu de 4 para 2 pontos.
- Cura de pickup caiu para 22 pontos.
- Mercado ficou mais caro e o reparo principal caiu para 34% do casco.

### Três raridades reais

Todo perk/habilidade agora aparece em exatamente uma destas três raridades:

- **COMUM** — efeito base ×1,00.
- **RARO** — efeito ×1,35.
- **LENDÁRIO** — efeito ×1,80.

As três raridades foram observadas em bateria de 12 seeds. A raridade altera de fato a força da evolução; não é apenas cor de carta.

## QA v9

- Primeiro chefe: aparece ~33 s e leva ~38 s de combate contínuo no robô de QA.
- Progressão: ~nível 3 aos 60 s; ~nível 7 aos 120 s; nas 12 seeds de 150 s, nível 7–9.
- Stress de chefe 3×3 fases:
  - touch: pico 162 / limite 200;
  - desktop retrato: pico 329 / limite 330;
  - desktop paisagem: pico 306 / limite 330.
- Paleta hostil: somente rampa rosa.
- Regressão longa de quatro núcleos: 0 exceções.
- `node --check`: PASS.

## Google Drive

Pasta do projeto:
https://drive.google.com/drive/folders/14JSsgfglD3oEIyzK8eKm6v5ibFJuL8h9

HTML v9:
https://drive.google.com/file/d/1gg6Z9gxNH01BYg2Ly4YTM53QbXRVhQ82/view?usp=drivesdk

## Próximo passo

Teste humano da v9 no celular. Ajustar apenas a sensação real de dificuldade e duração de luta; não reduzir a pressão por reflexo sem evidência de uma morte injusta.