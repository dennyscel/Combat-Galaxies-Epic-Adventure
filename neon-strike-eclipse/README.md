# Neon Strike: Eclipse Protocol — v5 STOLEN TECH

Linha atual de desenvolvimento do shooter single-file, preservando o Combat Galaxies histórico e o checkpoint v4.

## Base canônica

- Jogo: `neon_strike_eclipse_protocol_v5_stolen_tech.html`
- Tamanho: ~211 KB.
- SHA-256: `b224de4c77956343a52018c942c28eee2d06053a077a4a581b57d4f9bca158fb`.
- Arquivo único, sem CDN, imports ou assets externos.
- Save: `neon_strike_eclipse_v5`, com migração silenciosa de v4/v3/v2.

## Gancho central

> Você não mata o chefe. Você o desmonta e veste as peças.

- Arconte: 2 prismas.
- Tecelã: 3 casulos.
- Leviatã: 2 canhões.
- Matar o núcleo antes destrói partes restantes sem loot.
- Peças mudam silhueta e arma da nave.

## v5 — tecnologia roubada

A construção agora tem **21 evoluções + 14 fusões = 35 opções**. Nove fusões dependem diretamente das peças roubadas:

- Estilhaço Vorpal
- Lente de Caça
- Teia Voltaica
- Guarda de Casulo
- Ninho Caçador
- Câmara de Cerco
- Recuo Cinético
- Motor de Sucata
- Protocolo Eclipse

`Protocolo Eclipse` exige pelo menos um prisma, um casulo e um canhão e sincroniza as três famílias de tecnologia roubada a cada oitava rajada.

## QA v5

- `node --check`: PASS.
- 14/14 fusões ativáveis: PASS.
- Stress real Chromium com canvas: 39 projéteis touch / 44 desktop no pico observado; 0 erros.
- Paleta hostil observada somente dentro da rampa rosa.
- Robô acelerado de 300 s em touch portrait, desktop portrait e landscape: 3/3 chefes cobertos em todas as configurações.
- Heap touch 600 s após GC: 2.655.900 bytes em 300 s → 2.917.988 bytes em 600 s; crescimento pós-aquecimento de ~0,26 MB.
- Android físico 10 min: ainda pendente.
- Baseline aprovada para screenshot regression: ainda pendente.

O QA interno pode ser ativado com `?qa=1`; seed reproduzível continua disponível com `?seed=<n>`.

## Google Drive — fonte e pacote completo

Pasta do projeto:
https://drive.google.com/drive/folders/14JSsgfglD3oEIyzK8eKm6v5ibFJuL8h9

HTML v5:
https://drive.google.com/file/d/1eHkKvkbyTNxi3nh2990IuvX4dCtmCoKZ/view?usp=drivesdk

ZIP v5:
https://drive.google.com/file/d/1Ot4-8QkgvxGZNushQhwHP28vfKtXIEua/view?usp=drivesdk

Régua v3:
https://drive.google.com/file/d/1H1JHgk_VaT26-nsre_g2n7QKyL261wth/view?usp=drivesdk

QA v5:
https://drive.google.com/file/d/19ckxevl2mLhMYuSywCvve4tk5YJwdyX7/view?usp=drivesdk

Screenshot mobile v5:
https://drive.google.com/file/d/1f_48lBS5hODLG7EKpuuQxVQAeNn8HkYL/view?usp=drivesdk

## Próximo alvo

A amplitude de construção deixou de ser a maior fraqueza. A próxima iteração deve atacar **identidade visual de atos e antecipação dos padrões pela postura do chefe**, sem adicionar conteúdo genérico.