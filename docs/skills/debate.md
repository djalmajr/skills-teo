# debate

Agent source of truth: [`skills/debate/SKILL.md`](../../skills/debate/SKILL.md)

## When to use

- `/teo-debate`
- Mediar debate entre escolas
- Entrevistar o tema (perguntas estruturadas) e só então lançar
- Testar uma tese *deste* debate contra três leituras rivais
- Rodar três agentes no Herdr e guardar o resultado
- Escatologia: amilenarismo × pré-milenarismo histórico × dispensacionalismo clássico

## When not to use

- Sermão ou artigo de uma só voz (`sermao`)
- Um agente fingindo três chapéus no mesmo fio
- Exegese sem confronto de escolas
- Escrever o livro (`livro`) — mesmo que o insumo venha a ser este debate

## Assets

- `references/intake.md` — grill obrigatório (`ask_user_question`) antes de criar pasta ou lançar
- `references/elencos.md` — catálogo padrão e critério de elenco
- `references/metodo-quatro-pontos.md` — protocolo calibrado em Grudem (ed.), *Cessaram os dons espirituais?*
- `templates/` — índice, protocolo, brief, peça, atas, qualidade, curadoria, síntese, veredito, aprendizados
- `examples/` — forma de peça e de quadro (não doutrina para copiar)

## Output layout (user working folder)

```text
<destino>/
├── indice.md     # porta (tema, pergunta, vozes); aponta síntese + veredito + turnos
└── raw/          # protocolo, turnos, atas, qualidade, síntese, veredito, curadoria
```

O dossiê não cita nota ou artigo fora desta pasta. O produto é o **debate** (síntese + veredito + peças). Não há `livro/` aqui. Volume é a skill `livro`, outra pasta, outro ciclo.

## Evolution

Depois de um debate real, `aprendizados.md` lista falhas de protocolo. Patches entram nesta skill com evidência de uso, não no calor da sessão.
