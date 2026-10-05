# teo-livro

Fonte de verdade da skill: [`skills/teo-livro/SKILL.md`](../../skills/teo-livro/SKILL.md)

## Quando usar

- `/teo-livro`
- Escrever um livro ou livro digital (AsciiDoc)
- Extrair um volume de um debate já fechado, de notas, de artigo ou de um tópico nu
- Quatro perspectivas *literárias* (pedagogia, não ata)

## Quando não usar

- Mediar o debate (`teo-debate`)
- Sermão (`teo-sermao`)
- Transcrever vídeo (`teo-transcricao`)

O debate, se existir, é **insumo opcional**. O volume vive em outra pasta (`Livro - <tema>/`). A skill de debate não compila livro.

## Recursos

- `references/intake.md` — entrevista inicial antes de rascunhar
- `references/prosa.md` — fio, parágrafo, esboço reverso
- `references/estruturas.md` — quatro pontos, inquérito, voz única
- `references/bancada.md` — pesquisador, arquiteto, redator, editores
- `templates/` — orientação, pesquisa, plano de capítulos, esboço reverso, edição, curadoria, `_index.adoc`

## Estrutura de saída (pasta de trabalho)

```text
<destino>/
├── indice.md     # porta (pergunta, fio, leitor)
├── livro/        # AsciiDoc: _index.adoc + um .adoc por capítulo
└── raw/          # pesquisa, plano de capítulos, edição, curadoria
```

O processo (pesquisa → plano de capítulos → piloto → bancada → compilação) é obrigatório. Compilar não basta.
