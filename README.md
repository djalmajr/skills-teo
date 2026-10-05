# skills-teo

Skills teológicas e pastorais para agentes de IA.

Repositório: https://github.com/djalmajr/skills-teo

## Instalação

Use a CLI `skills`. `bunx` é preferível; `npx` também funciona.

A abreviação `djalmajr/skills-teo` abaixo usa a sintaxe `owner/repo` do GitHub para o repositório público: https://github.com/djalmajr/skills-teo

As notas detalhadas de distribuição e atualização estão em [`docs/distribution.md`](docs/distribution.md).

```bash
# Todas as skills
bunx skills add djalmajr/skills-teo --skill '*'

# Skills específicas
bunx skills add djalmajr/skills-teo --skill teo-sermao
bunx skills add djalmajr/skills-teo --skill teo-transcricao
bunx skills add djalmajr/skills-teo --skill teo-debate
bunx skills add djalmajr/skills-teo --skill teo-livro

# Agentes de destino explícitos
bunx skills add djalmajr/skills-teo --agent claude-code --agent opencode --agent codex --skill '*'
```

## Estrutura do pacote

Este repositório segue a convenção compartilhada de Agent Skills:

```text
skills/<nome-da-skill>/SKILL.md          # skills autorais distribuídas
skills/<nome-da-skill>/scripts/          # auxiliares opcionais da skill
skills/<nome-da-skill>/templates/        # esqueletos opcionais de saída
skills/<nome-da-skill>/references/       # catálogos e tabelas de consulta opcionais
skills/<nome-da-skill>/examples/         # material opcional de calibração
skills/<nome-da-skill>/transcriptions/   # amostras opcionais de voz em formato longo
.agents/skills/<nome-da-skill>/SKILL.md  # skills de terceiros explicitamente vendorizadas, se houver
```

`SKILL.md` é a fonte de verdade para o comportamento dos agentes, os gatilhos e o procedimento de execução. O README raiz explica o pacote para pessoas; as notas humanas específicas de cada skill ficam em `docs/skills/`.

Skills de terceiros ficam fora do diretório canônico `skills/` do projeto e fora de `skills.json`. Somente caminhos explicitamente excluídos das regras de arquivos ignorados em `.agents/skills/` seriam versionados; as demais skills instaladas localmente continuam ignoradas.

## Compatibilidade

Estas skills usam o formato comum `SKILL.md`, adotado por `skills.sh`, Claude Code, OpenCode e Codex.

- `skills.sh` descobre as skills autorais do projeto em `skills/` e as instala nos caminhos dos agentes selecionados.
- Claude Code carrega skills instaladas de `.claude/skills/<name>/SKILL.md` ou `~/.claude/skills/<name>/SKILL.md`.
- OpenCode carrega skills dos caminhos `.opencode/skills`, `.claude/skills` ou `.agents/skills` e exige que `name` corresponda ao nome do diretório.
- Codex lê os mesmos metadados de `SKILL.md`.

Mantenha o bloco de metadados portátil. Evite campos específicos de agentes, a menos que a skill realmente precise deles e o comportamento esteja documentado em `SKILL.md`.

`sermao-emilio` foi renomeada para `teo-sermao`. A voz de Garófalo é `--estilo=emilio` (o padrão).

## Skills (4)

| Skill | Finalidade |
|-------|---------|
| `teo-debate` | Entrevista o tema, media três agentes, grava ata + síntese + veredito. **Não** escreve o livro. |
| `teo-livro` | Escreve um volume (livro digital em AsciiDoc) com pesquisa, fio, editores e curadoria. Insumo opcional: um debate, notas, artigo ou tópico nu. |
| `teo-sermao` | Cria sermões pregáveis; o estilo é parâmetro (`emilio`, `expositivo` ou ad hoc). |
| `teo-transcricao` | Fluxo YouTube → legendas → texto limpo → artigo em prosa; organiza `raw/` + `artigos/`. |

## Fluxo

```text
texto bíblico / URL  →  teo-sermao (pregável)  ou  teo-transcricao (artigo)

entrevista inicial (tema, pergunta, tese)  →  teo-debate  →  Debate - tema/ (indice + raw)
                                                      ↓  opcional, outra pasta
                                                   teo-livro  →  Livro - tema/ (indice + livro/_index.adoc + raw)
```

## Convenção de modelos e recursos

Cada skill mantém seus próprios auxiliares em `skills/<nome-da-skill>/` (`scripts/`, `examples/`, `transcriptions/`, `templates/` quando necessário). Os arquivos `SKILL.md` devem referenciar esses caminhos de forma relativa. Não dependa de caminhos absolutos globais ou pastas pessoais; as skills precisam ser autossuficientes quando instaladas.

Referências a repositórios externos devem usar links completos do GitHub na documentação quando for prático. Abreviações como `djalmajr/skills-teo` são aceitáveis somente onde uma CLI espera a sintaxe `owner/repo` do GitHub.

## Ciclo de evolução das skills

Trate estas skills como um kit pastoral vivo. As melhorias devem vir de evidências de uso real: aberturas fracas, metadados ausentes, scripts frágeis de limpeza ou saídas que falham em um teste rápido de pregação/leitura. Mantenha as mudanças pequenas e rastreáveis, atualize o `SKILL.md` afetado e os recursos locais em conjunto e valide pelo menos um caso realista antes da publicação.

## Lista de verificação antes da publicação

Antes de publicar ou pedir que as pessoas atualizem skills instaladas:

- Cada diretório de skill em `skills/` tem um `SKILL.md`.
- Cada `SKILL.md` começa com metadados YAML válidos.
- O `name` do bloco de metadados corresponde ao nome do diretório.
- A `description` do bloco de metadados explica o que a skill faz e quando usá-la.
- `skills.json`, se mantido, lista cada diretório de skill e não omite skills nem mantém nomes antigos.
- A documentação humana em `docs/` aponta para `docs/skills/*.md`.
- Modelos ou scripts novos ficam dentro do diretório da skill proprietária.
- O conteúdo reutilizável das skills não depende de caminhos absolutos locais, repositórios privados ou nomes específicos de máquinas.
- Um teste de instalação para os agentes de destino é feito com `bunx skills add ...` antes da publicação.

Veja a lista de verificação completa de publicação e atualização em [`docs/distribution.md`](docs/distribution.md).

## Documentação

[`docs/`](docs/) — guias de uso para pessoas. As notas específicas de cada skill ficam em [`docs/skills/`](docs/skills/).

## Como usar

Cada skill é invocada com `/teo-<nome>`:

```text
/teo-sermao
/teo-sermao --estilo=emilio
/teo-transcricao
/teo-debate
/teo-livro
```
