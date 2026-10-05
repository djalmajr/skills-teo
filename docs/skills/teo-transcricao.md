# teo-transcricao

Fonte de verdade da skill: [`skills/teo-transcricao/SKILL.md`](../../skills/teo-transcricao/SKILL.md)

## Quando usar

- `/teo-transcricao`
- Transcrever sermão/exposição/aula do YouTube
- Processar playlist ou lote de URLs
- Limpar `.srt`/`.vtt` com eco de auto-legenda
- Reescrever oralidade em artigo Markdown

## Quando não usar

- Criar sermão novo sem fonte em áudio/vídeo
- Baixar o vídeo completo sem necessidade
- Entregar estenotipia com marcações de tempo como produto final

## Recursos

- `scripts/limpar_legendas.py` — mesclagem de legendas rolantes do reconhecimento automático de fala (ASR) e texto corrido

## Estrutura de saída (pasta de trabalho)

```text
<colecao>/
├── README.md
├── artigos/
└── raw/
    ├── legendas-brutas/
    └── textos-limpos/
```
