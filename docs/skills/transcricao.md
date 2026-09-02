# transcricao

Agent source of truth: [`skills/transcricao/SKILL.md`](../../skills/transcricao/SKILL.md)

## When to use

- `/teo-transcricao`
- Transcrever sermão/exposição/aula do YouTube
- Processar playlist ou lote de URLs
- Limpar `.srt`/`.vtt` com eco de auto-legenda
- Reescrever oralidade em artigo Markdown

## When not to use

- Criar sermão novo sem fonte em áudio/vídeo
- Baixar o vídeo completo sem necessidade
- Entregar estenotipia com timestamps como produto final

## Assets

- `scripts/limpar_legendas.py` — merge de rolling ASR e texto corrido

## Output layout (user working folder)

```text
<colecao>/
├── README.md
├── artigos/
└── raw/
    ├── legendas-brutas/
    └── textos-limpos/
```
