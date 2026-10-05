# Distribuição

## Fonte

- Repositório público: https://github.com/djalmajr/skills-teo
- Abreviação de instalação para a CLI `skills`: `djalmajr/skills-teo`

## Instalação

```bash
# Todas as skills
bunx skills add djalmajr/skills-teo --skill '*'

# Uma skill
bunx skills add djalmajr/skills-teo --skill teo-sermao
bunx skills add djalmajr/skills-teo --skill teo-transcricao
bunx skills add djalmajr/skills-teo --skill teo-debate
bunx skills add djalmajr/skills-teo --skill teo-livro

# Agentes explícitos
bunx skills add djalmajr/skills-teo --agent claude-code --agent opencode --agent codex --skill '*'
```

`npx skills add ...` também funciona quando `bunx` não estiver disponível.

## Contrato portátil

As skills distribuídas ficam em:

```text
skills/<nome-da-skill>/SKILL.md
skills/<nome-da-skill>/scripts/          # opcional
skills/<nome-da-skill>/templates/        # opcional
skills/<nome-da-skill>/references/       # opcional
skills/<nome-da-skill>/examples/         # opcional
skills/<nome-da-skill>/transcriptions/   # opcional
```

Regras:

1. Cada diretório de skill tem um `SKILL.md`.
2. O `name` do bloco de metadados corresponde ao nome do diretório.
3. A `description` do bloco de metadados declara a capacidade e o contexto de acionamento.
4. Os recursos referenciados por uma skill permanecem dentro do diretório dela (ou usam caminhos relativos a ele).
5. Não codifique caminhos de máquina, pastas pessoais, árvores privadas de notas ou segredos específicos do ambiente.
6. `skills.json` lista cada skill autoral do projeto sob a fonte `djalmajr/skills-teo`.

## O que é distribuído

- `skills/*/SKILL.md` e os auxiliares pertencentes às skills
- `README.md` raiz
- `docs/`
- `skills.json` / `package.json` opcionais

## O que não é distribuído como conteúdo do pacote

- Caches de skills instaladas localmente (`.claude/`, `.codex/`, a maior parte de `.agents/`)
- Coleções de trabalho geradas por `teo-transcricao` (`raw/`, `artigos/`), `teo-debate` (`Debate - …/`) ou `teo-livro` (`Livro - …/`), a menos que a pessoa usuária escolha mantê-las em outro lugar
- Arquivos de bloqueio produzidos por instalações locais (`skills-lock.json`)

## Fluxo de atualização

1. Altere a skill e quaisquer recursos locais relacionados em conjunto.
2. Rode `npm test` (inventário de skills + verificações de metadados).
3. Crie uma ramificação de trabalho para as mudanças.
4. Abra uma solicitação de integração (PR) da ramificação para `main`.
5. Aguarde a execução e a aprovação das verificações do PR.
6. Faça a integração em `main` somente com autorização.
7. As pessoas consumidoras atualizam com `bunx skills add djalmajr/skills-teo --skill '*'`.

A migração do repositório não atualiza instalações existentes. Uma instalação anterior pode continuar com uma cópia sem o prefixo `teo-`, criando duplicatas; remova ou atualize essas cópias conforme o gerenciador e o agente de destino.

## Lista de verificação antes da publicação

- [ ] Cada diretório em `skills/` tem um `SKILL.md`
- [ ] Cada `SKILL.md` começa com metadados YAML
- [ ] O `name` do bloco de metadados corresponde ao nome do diretório
- [ ] A `description` do bloco de metadados cobre a capacidade e quando usar
- [ ] `skills.json` lista cada diretório de skill
- [ ] A documentação humana em `docs/skills/` está sincronizada com os nomes das skills
- [ ] Modelos/scripts ficam dentro da skill proprietária
- [ ] Não há caminhos absolutos locais, repositórios privados, tokens ou nomes de máquinas pessoais nos arquivos distribuídos
- [ ] Teste de instalação com `bunx skills add djalmajr/skills-teo ...`
