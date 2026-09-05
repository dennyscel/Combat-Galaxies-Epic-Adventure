# Régua — estado v6 THREE ACTS

Base canônica: `neon_strike_eclipse_protocol_v6_three_acts.html`.

## Gancho

Preservado: Arconte 2 prismas, Tecelã 3 casulos, Leviatã 2 canhões. Matar o núcleo antes continua destruindo partes restantes sem loot. A nave veste as peças e elas alimentam as fusões de tecnologia roubada.

## Construção

- 21 perks;
- 14 fusões comportamentais;
- 35 opções totais;
- 9 fusões dependem das peças roubadas.

## Identidade visual v6

- 3/3 atos: Corredor de Íons, Campo de Fratura, Forja do Eclipse;
- paleta ambiental `ENV` neutra dessaturada, separada das cores semânticas;
- 6 posturas/intenções antes do padrão: fan, radial, laser, field, ram, summon;
- summon não letal usa ENV; intenções letais usam rosa.

## Justiça

- arming do projétil: 0,60 s;
- telegraph de intenção do chefe: 0,72 s;
- hard cap hostil: 200 touch / 330 desktop;
- stress dirigido: pico 52/52;
- robô 300 s: picos 127 / 174 / 329, todos dentro da régua.

## Técnico

- arquivo único, sem assets/dependências externas;
- RNG gameplay/visual separado;
- seed reproduzível;
- 0 erros não tratados nas baterias finais;
- heap 300→600 s após GC: +76.112 bytes na medição final.

## Pendências

- Android físico 10 min;
- avaliação humana da sensação sonora/impacto;
- baseline histórica aprovada de screenshot regression.

O próximo crítico deve procurar a menor dimensão restante; não adicionar conteúdo genérico antes disso.