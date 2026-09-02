# livro

Agent source of truth: [`skills/livro/SKILL.md`](../../skills/livro/SKILL.md)

## When to use

- `/teo-livro`
- Escrever um livro ou ebook (AsciiDoc)
- Extrair um volume de um debate já fechado, de notas, de artigo, ou de um tópico nu
- Four Views *literário* (pedagogia, não ata)

## When not to use

- Mediar o debate (`debate`)
- Sermão (`sermao`)
- Transcrever vídeo (`transcricao`)

O debate, se existir, é **insumo opcional**. O volume vive em pasta **outra** (`Livro - <tema>/`). A skill de debate não compila livro.

## Assets

- `references/intake.md` — grill antes de rascunhar
- `references/prosa.md` — fio, parágrafo, reverse outline
- `references/estruturas.md` — quatro-pontos, inquérito, voz-única
- `references/bancada.md` — pesquisador, arquiteto, redator, editores
- `templates/` — brief, pesquisa, outline, reverse outline, edição, curadoria, `_index.adoc`

## Output layout (user working folder)

```text
<destino>/
├── indice.md     # porta (pergunta, fio, leitor)
├── livro/        # AsciiDoc: _index.adoc + um .adoc por capítulo
└── raw/          # pesquisa, outline, edição, curadoria
```

O processo (pesquisa → outline → piloto → bancada → compile) é obrigatório. Compilar não basta.
