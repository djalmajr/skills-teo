# teo-debate

Fonte de verdade da skill: [`skills/teo-debate/SKILL.md`](../../skills/teo-debate/SKILL.md)

## Quando usar

- `/teo-debate`
- Mediar debate entre escolas
- Fazer a entrevista inicial do tema (perguntas estruturadas) e só então iniciar
- Testar uma tese *deste* debate contra três leituras rivais
- Rodar três agentes no Herdr e guardar o resultado
- Escatologia: amilenarismo × pré-milenarismo histórico × dispensacionalismo clássico

## Quando não usar

- Sermão ou artigo de uma só voz (`teo-sermao`)
- Um agente fingindo três chapéus no mesmo fio
- Exegese sem confronto de escolas
- Escrever o livro (`teo-livro`), mesmo que o insumo venha a ser este debate

## Recursos

- `references/intake.md` — entrevista inicial obrigatória (`ask_user_question`) antes de criar pasta ou iniciar
- `references/elencos.md` — catálogo padrão e critério de elenco
- `references/metodo-quatro-pontos.md` — protocolo calibrado em Grudem (ed.), *Cessaram os dons espirituais?*
- `templates/` — índice, protocolo, orientação, peça, atas, verificação de qualidade, curadoria, síntese, veredito, aprendizados
- `examples/` — forma de peça e de quadro (não doutrina para copiar)

## Estrutura de saída (pasta de trabalho)

```text
<destino>/
├── indice.md     # porta (tema, pergunta, vozes); aponta síntese + veredito + turnos
└── raw/          # protocolo, turnos, atas, qualidade, síntese, veredito, curadoria
```

O dossiê não cita nota ou artigo fora desta pasta. O produto é o **debate** (síntese + veredito + peças). Não há `livro/` aqui. O volume é responsabilidade de `teo-livro`, em outra pasta e outro ciclo.

## Evolução

Depois de um debate real, `aprendizados.md` lista falhas de protocolo. Patches entram nesta skill com evidência de uso, não no calor da sessão.
