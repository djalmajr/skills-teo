# sermao

Agent source of truth: [`skills/sermao/SKILL.md`](../../skills/sermao/SKILL.md)

Renomeou `sermao-emilio`. O estilo Garófalo continua como **estilo** `emilio`.

## When to use

- `/teo-sermao`
- Preparar sermão, esboço ou manuscrito oral
- `/teo-sermao --estilo=emilio` ou “estilo Emílio/Garófalo”
- `/teo-sermao --estilo=expositivo` quando a ossatura deve ser o próprio texto

## When not to use

- Estudo exegético técnico sem intenção de pregação
- Artigo acadêmico
- Transcrição de vídeo (`transcricao`)

## Parameters

| Param | Default | Notes |
|---|---|---|
| `estilo` | `emilio` | Catálogo: `references/estilos.md`. Flag: `--estilo=` |
| `texto` | — | Obrigatório |
| `ocasiao`, `publico`, `duracao`, `formato` | ver skill | |

## Assets

- `estilos/emilio.md` + `estilos/emilio/examples/` + `transcriptions/`
- `estilos/expositivo.md`
- `references/contrato-estilo.md` — como acrescentar um estilo

## Output

Artefato pregável no formato **do estilo escolhido**, com `**Estilo:**` no topo.
