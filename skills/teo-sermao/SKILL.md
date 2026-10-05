---
name: teo-sermao
description: >-
  Cria, reescreve ou estrutura sermões pregáveis. O estilo é um parâmetro (catálogo em estilos/): emilio (narrativo-pastoral de Emílio Garófalo Neto), expositivo (segue o texto sem história-porta obrigatória), ou estilo ad hoc descrito pelo usuário. Use quando pedir sermão, esboço de pregação, homilia, mensagem dominical, manuscrito oral, "sermão no estilo Emílio/Garófalo", /teo-sermao, /teo-sermao --estilo=emilio, ou /teo-sermao-emilio.
---

# Sermão

Produza um sermão **pregável**. O texto bíblico governa. O **estilo** define voz, arco e artefato.

Não use esta skill para artigo acadêmico, exegese sem intenção de pregação, transcrição de exposição existente (`teo-transcricao`), debate entre escolas (`teo-debate`), nem livro digital (`teo-livro`).

## Parâmetros

| Campo | Obrigatório? | Como entra | Padrão |
|---|---|---|---|
| `texto` | sim | referência ou passagem | — (pergunte) |
| `estilo` | recomendado | `--estilo=emilio`, “estilo emilio”, “estilo Garófalo”, “expositivo” | `emilio` (declare no artefato) |
| `ocasiao` | recomendado | culto, conferência, santa ceia, funeral | declare o que inferir |
| `publico` | recomendado | igreja mista, jovens, famílias | igreja local adulta/mista |
| `duracao` | opcional | 25 / 35 / 45 min | 30–40 min |
| `formato` | opcional | esboço, manuscrito, ambos | manuscrito oral + esboço curto |
| `enfase` | opcional | consolo, correção, missão… | a do texto |
| `restricoes` | opcional | sem humor, evitar futebol… | nenhuma |

Sobreposições do usuário vencem o estilo (ex.: `estilo=emilio` + “sem humor”).

## Resolver o estilo

1. Leia `references/estilos.md`.
2. Case o pedido com `id` ou aliases. `/teo-sermao-emilio` e “Garófalo” → `emilio`.
3. Leia **por inteiro** `estilos/<id>.md`. Se o estilo tiver `examples/` ou `transcriptions/`, use-os como o arquivo mandar.
4. Sem estilo e sem pista: `emilio`, declarado no topo (`**Estilo:** emilio`).
5. Estilo **ad hoc** (o usuário descreve a voz e não há id): leia `references/contrato-estilo.md`, monte um estilo mínimo na hora, declare `**Estilo:** ad-hoc — <uma linha>`. Não finja que é `emilio` se o usuário recusou história-porta.
6. Id desconhecido: liste o catálogo e pergunte. Não invente um perfil.

## Invariantes (qualquer estilo)

- Escritura governa; não invente doutrina, ilustração “bíblica” ou aplicação ausente do texto.
- Idioma do usuário. Em pt-BR: oral cultual, não jargão de seminário.
- Tese pregável cedo, não título acadêmico.
- Fecho de graça, não lista moralista — salvo o usuário pedir outro encerramento.
- Sem recursos infantis / dinâmica de público por padrão.
- Declare metadados no topo, incluindo **Estilo:**.

## Fluxo

1. Obter `texto` (e o resto da tabela). Sem texto, pergunte.
2. Resolver e carregar o estilo.
3. Ouvir o texto (contexto, tensão humana, ação de Deus, resposta da fé, tese em 1 frase).
4. Seguir o **fluxo e o artefato do estilo**. Não misture arco de `emilio` num pedido `expositivo`.
5. Revisar com a lista de verificação do estilo.
6. Entregar. Uma linha de variações no fim (mais curto / outro estilo), sem enrolar.

## Resposta ao usuário

1. Falta texto → pergunte.
2. Senão, artefato completo no formato do estilo.
3. Não recorra a `teo-debate` (várias escolas), `teo-transcricao` (vídeo → artigo) nem `teo-livro` (volume).
