# Régua — estado v4 GAUNTLET

A régua completa está preservada no Google Drive. Este arquivo registra somente o delta verificado da nova base.

## Gancho
**IMPLEMENTADO E TESTADO 3/3.**

- Arconte: 2 prismas.
- Tecelã: 3 casulos.
- Leviatã: 2 torres → canhões.
- Parte quebrada larga módulo temporário.
- Matar o chefe antes destrói peças restantes sem loot.
- Peças vestidas alteram silhueta e arma.

## Invariantes reforçados
- arquivo único: PASS
- dependência externa: 0
- projéteis hostis na rampa rosa: PASS no stress amostrado
- telegraph de chefe: 0,68 s
- arming hostil: 0,60 s
- modo reduzir flashes preservado
- toque/teclado/controle preservados

## Construção
A v4 adiciona 5 fusões de comportamento: Leque Rail, Tempestade Crítica, Matilha Vetorial, Coroa Sentinela e Corte de Fase.

O alvo continua maior: chegar a uma árvore em que a maior parte das escolhas altere comportamento, não apenas porcentagem.

## Primeiros 60 segundos
O primeiro chefe foi antecipado para o setor 3 para mostrar o gancho antes.

## Determinismo
- PRNG de gameplay separado do PRNG visual
- seed por `?seed=<n>`
- seed registrada no recap

## Evidência desta iteração
- Chromium mobile 390×844: 0 erros
- Chromium desktop 1280×720: 0 erros
- stress touch 3 chefes × 3 fases: pico 57 projéteis
- limite da régua mobile: ≤200

## Pendente obrigatório
- 10 minutos em Android físico intermediário
- heap de 600 s em hardware
- cobertura exaustiva de cada repertório
- diff visual automático entre versões

Régua completa:
https://drive.google.com/file/d/14Jm1aU9L3I3Yg263_WipDSgwBXKZ2SJ-/view?usp=drivesdk
