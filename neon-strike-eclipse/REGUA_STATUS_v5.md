# Régua — estado v5 STOLEN TECH

Base canônica: `neon_strike_eclipse_protocol_v5_stolen_tech.html`.

## Invariantes

- Arquivo único: PASS.
- Zero dependências externas: PASS.
- Rampa de ameaça hostil: PASS na bateria observada.
- Arming de projéteis e telegraph de chefe preservados da v4.
- Qualidade adaptativa continua sem reduzir gameplay.
- Save v5 migra de v4/v3/v2.

## Gancho

> Você não mata o chefe. Você o desmonta e veste as peças.

- Arconte: 2 prismas.
- Tecelã: 3 casulos.
- Leviatã: 2 canhões.
- Rush no núcleo continua eliminando partes restantes sem loot.
- Silhueta e arma do jogador mudam com as peças.

## Profundidade

- 21 perks.
- 14 fusões comportamentais.
- 9 fusões dependentes de tecnologia roubada.
- 35 opções totais.
- `Protocolo Eclipse` exige as três famílias de peças.

A amplitude de construção deixa de ser a maior fraqueza desta iteração.

## Evidência objetiva

- stress Chromium real: 39 projéteis touch / 44 desktop;
- 0 erros não tratados;
- robô 300 s: 3/3 chefes em touch portrait, desktop portrait e landscape;
- heap touch 300→600 s após GC: +262.088 bytes;
- setor 28 em simulação de 600 s.

## Pendências

- Android físico 10 min;
- screenshot regression com baseline aprovada por humano;
- validação humana da sensação sonora.

## Nova maior fraqueza

**Identidade visual de atos + postura de chefe que antecipe o padrão antes do primeiro disparo.**

Não adicionar inimigo, chefe ou perk genérico antes de atacar essa dimensão.