# teo-sermao

Fonte de verdade da skill: [`skills/teo-sermao/SKILL.md`](../../skills/teo-sermao/SKILL.md)

`sermao-emilio` foi renomeada. O estilo Garófalo continua como **estilo** `emilio`.

## Quando usar

- `/teo-sermao`
- Preparar sermão, esboço ou manuscrito oral
- `/teo-sermao --estilo=emilio` ou “estilo Emílio/Garófalo”
- `/teo-sermao --estilo=expositivo` quando a estrutura deve ser o próprio texto

## Quando não usar

- Estudo exegético técnico sem intenção de pregação
- Artigo acadêmico
- Transcrição de vídeo (`teo-transcricao`)

## Parâmetros

| Parâmetro | Padrão | Observações |
|---|---|---|
| `estilo` | `emilio` | Catálogo: `references/estilos.md`. Flag: `--estilo=` |
| `texto` | — | Obrigatório |
| `ocasiao`, `publico`, `duracao`, `formato` | ver skill | |

## Recursos

- `estilos/emilio.md` + `estilos/emilio/examples/` + `transcriptions/`
- `estilos/expositivo.md`
- `references/contrato-estilo.md` — como acrescentar um estilo

## Saída

Artefato pregável no formato **do estilo escolhido**, com `**Estilo:**` no topo.
