---
name: livro
description: >-
  Escreve um livro (ebook em AsciiDoc) com o processo de um volume real:
  pesquisa do insumo, fio condutor, outline por capítulo, rascunho, editor
  de desenvolvimento, revisor de linha, checagem de fontes, copydesk e
  curadoria. Use quando pedir livro, ebook, volume didático, "escreve um
  livro sobre", Four Views literário, AsciiDoc de livro, ou /teo-livro. Pode
  tomar um debate como insumo, ou qualquer outro tópico. Não
  media o debate (isso é debate) nem escreve sermão (sermao).
---

# Livro

Escreva um **livro**. Não um relatório, não um digest, não a ata de um debate.

O debate, se existir, é **insumo opcional**. Esta skill não o substitui e não o reabre. Se o usuário ainda não tem disputa entre escolas e a quer, pare e aponte `debate`. Depois, se quiser o volume, volte aqui.

Não seja preguiçoso com o insumo. Sem leitura integral das fontes nomeadas, não há outline.

## Quando usar

- Pedido de livro, ebook, volume, «escreve um livro sobre»
- Extrair um livro de um debate já fechado (`Debate - …/`)
- Extrair um livro de notas, artigo (`transcricao`), tese, ou pergunta
- Four Views *literário* (uma leitura, depois quem responde *àquela* leitura)

## Quando NÃO usar

- Mediar três escolas (`debate`) — aqui não se lançam debatedores
- Sermão pregável (`sermao`)
- Transcrever vídeo (`transcricao`)
- Digest, resumo, ou «capítulo único que cobre tudo»

## Princípios

1. **Fio antes da prosa.** Sem throughline de ≤20 palavras e sem destino do volume, não se escreve capítulo.
2. **Ler o insumo de verdade.** Debate: protocolo, síntese, veredito **e todos os turnos**. Notas: cada arquivo nomeado. Tópico nu: pesquisa registrada em `raw/pesquisa.md`. Não outline a partir da memória nem só do mapa.
3. **Cada unidade tem um emprego.** Capítulo: começa, anda, senta. Parágrafo: uma tese local, evidência, fecho que prepara o próximo. Entre unidades: *portanto* ou *mas*, nunca *e então*.
4. **Quem escreveu não é o único olho.** Editor de desenvolvimento e checador de fontes são subagentes isolados (ou, no mínimo, um passe depois do rascunho, contra o texto, não contra a intenção).
5. **Não invente.** Se o insumo é um debate, não acrescente tese que o turno não sustentou. Se o insumo é outro, não invente citação, dado ou doutrina.
6. **Destino ≠ vencedor de escola.** Um livro de visões senta nas perguntas que carregam o resto e no que isso faz na igreja, salvo o usuário pedir juízo doutrinário.

Detalhe da prosa: `references/prosa.md`. Estruturas: `references/estruturas.md`. Bancada: `references/bancada.md`.

## Intake (antes de criar pasta ou rascunhar)

Rode `references/intake.md` com pergunta estruturada. Sem as respostas, pare.

| Campo | Obrigatório? | Default |
|---|---|---|
| Tema (uma frase) | sim | — |
| Insumo | sim | tópico nu (aí a pesquisa é o primeiro trabalho) |
| Leitor | sim | crente inteligente, sem diploma |
| Fio (≤20 palavras) + destino do volume | sim | — |
| Estrutura | sim (confirmar) | `quatro-pontos` se o insumo for debate; senão propor |
| Idioma | sim | português do Brasil |
| Pasta destino | sim | `Livro - <tema>/` no cwd |
| Autorização para escrever | sim | — |

Não misture pasta de debate com pasta de livro. O debate permanece onde está. O volume é **outra** pasta.

## Artefatos

```text
<destino>/
├── indice.md              # porta: pergunta, fio, leitor; aponta livro/_index.adoc
├── livro/                 # AsciiDoc: _index.adoc + um .adoc por capítulo
└── raw/
    ├── 00-brief.md        # fio, leitor, destino, insumo, estrutura
    ├── pesquisa.md        # o que foi lido, o que falta, fontes
    ├── outline.md         # emprego e destino de cada capítulo
    ├── reverse-outline.md
    ├── edicao.md          # desenvolvimento + linha
    └── curadoria.md
```

Copie a ossatura de `templates/`. Preencha; não deixe placeholder. Destino = o que o usuário pediu, senão cwd. Sem caminhos absolutos de máquina.

Capítulos incluídos começam em `==`. Subseções em `===` (não pule nível). `[[id]]` único, **começando por letra**. Glossário no fim, antes do índice remissivo. Título `= Tema: subtítulo` (a segunda linha do cabeçalho vira *autor* — não a use). Folha de rosto: pergunta e, se couber, vozes, num `[abstract]`. Sem `[dedication]`, sem página de autor, sem «como ler este arquivo».

## Ciclo

```text
intake → pesquisa (ler o insumo) → brief + outline
  → rascunho (um capítulo-piloto, depois o resto)
  → editor de desenvolvimento (reverse outline)
  → revisor de linha
  → checagem de fontes
  → copydesk (idioma, glossário, notas)
  → compile + curadoria
```

Não pule pesquisa. Não pule o reverse outline. Não declare o volume pronto só porque o AsciiDoc compila.

### 1. Pesquisa

Grave `raw/pesquisa.md` (`templates/pesquisa.md`).

- **Debate:** leia `00-protocolo.md`, `sintese.md`, `veredito.md` e **cada** `turnos/*.md`. Anote teses, concessões, perigos, textos de carga. A síntese não substitui os turnos.
- **Notas / artigos:** leia cada arquivo que o intake nomeou, por inteiro.
- **Tópico nu:** pesquise (Escritura no fio; fontes secundárias com referência). Registre o que foi aberto. Lacuna vira pergunta, não achismo.

Sem essa ficha, o outline é chute.

### 2. Brief e outline

`raw/00-brief.md`: fio, leitor, destino («depois destas páginas o leitor consegue…»), estrutura, o que o volume **não** é.

`raw/outline.md`: para cada capítulo, **emprego** (o que ele existe para fazer) e **destino** (o que o leitor deve poder dizer no fim). A sequência dos capítulos tem de ser *portanto* / *mas*. Capítulo que só «também trata de» sai ou muda de emprego.

Se o outline não sentar no fio, refaça o outline. Não escreva em cima de um mapa torto.

### 3. Rascunho

Comece por um **capítulo-piloto** (não o prefácio: um capítulo de miolo). Reverse-outline esse piloto (`references/prosa.md`). Só então escreva o resto.

Um `.adoc` por capítulo, extenso o bastante para sentar e ler. Idioma do brief (default pt-BR). Termo técnico inevitável: nota na primeira ocorrência **e** entrada no glossário.

Contrato de parágrafo e de capítulo: `references/prosa.md`. Não empilhe teses. Não circule.

### 4. Bancada (obrigatória)

Siga `references/bancada.md`. No mínimo:

1. **Editor de desenvolvimento** — subagente que **não** redigiu o capítulo. Reverse-outline do volume. RETRY se o capítulo não senta, se a sequência é *e então*, se o fio some.
2. **Checador de fontes** — cada declaração bíblica de carga: o texto diz o que a frase afirma? `não` → RETRY do capítulo. Alusão sem livro-capítulo-versículo → completar.
3. **Revisor de linha** — velho→novo, uma tese por parágrafo, conectivo real (não só «além disso»).

Grave o passe em `raw/edicao.md` e `raw/reverse-outline.md`.

### 5. Copydesk e produção

- pt-BR se o brief for pt-BR (sem ficheiro, ecrã, de facto)
- Glossário + notas de primeira ocorrência
- `asciidoctor livro/_index.adoc`
- `[[id]]` únicos; xrefs resolvem

### 6. Curadoria

`raw/curadoria.md` (`templates/curadoria.md`). Sem isso o volume não fechou. PASS / PASS com WARN / RETRY. Quem redigiu não é o único olho.

## Escritura

Toda declaração bíblica cita a fonte no fio (Jo 12.31; Jz 11.12). Nomear o livro ou o episódio não basta. Não invente referência.

## O que não entra no volume

Briefs, pesquisa, outline, reverse outline, edição, curadoria, nomes de pane, Herdr, T01, steelman. Isso fica em `raw/`. O leitor do livro não assiste ao processo.

Se o insumo for um debate: sem «nesta mesa», «o ensaio que se acabou de ler», «nós o ouvíamos», jargão de tribunal. A ordem dos quatro pontos de vista é pedagogia, não ata.

## Anti-padrões

- Compilar o livro dentro de `debate`
- Outline sem ter lido os turnos / as notas
- Capítulo que lista tópicos em vez de subir um degrau
- Parágrafo sem tese local (bloco de frases soltas)
- Sequência *e então* entre seções
- O mesmo agente como único editor do próprio rascunho
- Inventar tese, citação ou dado
- Digest, markdown único, ou capítulos curtos demais para sentar e ler
- Instrução de montagem no volume
- `[dedication]` ou página de autor em volume gerado
- Escolher vencedor de escola num livro de visões sem o usuário ter pedido
- Entregar sem `raw/curadoria.md` e sem compile

## Checklist

- [ ] Intake (tema, insumo, leitor, fio, destino, estrutura, idioma, destino, autorização)
- [ ] `raw/pesquisa.md` com fontes *lidas*, não listadas de memória
- [ ] Brief + outline: emprego e destino por capítulo
- [ ] Capítulo-piloto reverse-outlined antes do resto
- [ ] Editor de desenvolvimento isolado; reverse outline do volume
- [ ] Fontes de carga conferidas
- [ ] Glossário + notas de primeira ocorrência
- [ ] `asciidoctor` compila; xrefs resolvem
- [ ] `raw/curadoria.md` PASS ou PASS com WARN
