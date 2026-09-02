# skills-teo

Skills teológicas e pastorais para agentes de IA.

Repository: https://github.com/djalmajr/skills-teo

## Installing

Use the `skills` CLI. `bunx` is preferred; `npx` also works.

The `djalmajr/skills-teo` shorthand below is GitHub `owner/repo` syntax for the public repository: https://github.com/djalmajr/skills-teo

Detailed distribution and update notes live in [`docs/distribution.md`](docs/distribution.md).

```bash
# All skills
bunx skills add djalmajr/skills-teo --skill '*'

# Specific skills
bunx skills add djalmajr/skills-teo --skill sermao
bunx skills add djalmajr/skills-teo --skill transcricao
bunx skills add djalmajr/skills-teo --skill debate
bunx skills add djalmajr/skills-teo --skill livro

# Explicit target agents
bunx skills add djalmajr/skills-teo --agent claude-code --agent opencode --agent codex --skill '*'
```

## Package layout

This repo follows the shared Agent Skills convention:

```text
skills/<skill-name>/SKILL.md          # project-authored, distributed skills
skills/<skill-name>/scripts/          # optional helpers owned by the skill
skills/<skill-name>/templates/        # optional output skeletons
skills/<skill-name>/references/       # optional catalogs / lookup tables
skills/<skill-name>/examples/         # optional calibration material
skills/<skill-name>/transcriptions/   # optional long-form voice samples
.agents/skills/<skill-name>/SKILL.md  # explicitly vendored third-party skills (if any)
```

`SKILL.md` is the source of truth for agent behavior, triggers, and execution procedure. The root README explains the package for humans; skill-specific human notes live under `docs/skills/`.

Third-party skills stay out of the project's canonical `skills/` namespace and out of `skills.json`. Only explicitly unignored paths under `.agents/skills/` would be versioned; other locally installed agent skills remain ignored.

## Compatibility

These skills are written for the common `SKILL.md` format used by `skills.sh`, Claude Code, OpenCode, and Codex.

- `skills.sh` discovers project-authored skills under `skills/` and installs them into selected agent paths.
- Claude Code loads installed skills from `.claude/skills/<name>/SKILL.md` or `~/.claude/skills/<name>/SKILL.md`.
- OpenCode loads skills from `.opencode/skills`, `.claude/skills`, or `.agents/skills` locations and requires `name` to match the directory name.
- Codex reads the same `SKILL.md` metadata.

Keep frontmatter portable. Avoid agent-specific fields unless the skill truly needs them and the behavior is documented in `SKILL.md`.

`sermao-emilio` was renamed to `sermao`. The Garófalo voice is `--estilo=emilio` (the default).

## Skills (4)

| Skill | Purpose |
|-------|---------|
| debate | Entrevista o tema, media três agentes, grava ata + síntese + veredito. **Não** escreve o livro. |
| livro | Escreve um volume (ebook AsciiDoc) com pesquisa, fio, editores e curadoria. Insumo opcional: um debate, notas, artigo, ou tópico nu. |
| sermao | Cria sermões pregáveis; o estilo é parâmetro (`emilio`, `expositivo`, ou ad hoc) |
| transcricao | Pipeline YouTube → legendas → texto limpo → artigo em prosa; organiza `raw/` + `artigos/` |

## Flow

```text
texto bíblico / URL  →  sermao (pregável)  ou  transcricao (artigo)

intake (tema, pergunta, tese)  →  debate  →  Debate - tema/ (indice + raw)
                                                      ↓  opcional, outra pasta
                                                   livro  →  Livro - tema/ (indice + livro/_index.adoc + raw)
```

## Template and asset convention

Each skill owns its own helpers under `skills/<skill-name>/` (`scripts/`, `examples/`, `transcriptions/`, `templates/` when needed). `SKILL.md` files should reference those paths relatively. Do not rely on global absolute paths or personal folders; skills must be self-contained when installed.

External repo references should use full GitHub links in documentation when practical. Shorthands such as `djalmajr/skills-teo` are acceptable only where a CLI expects GitHub `owner/repo` syntax.

## Skill evolution loop

Treat these skills as a living pastoral toolkit. Improvements should come from real usage evidence: weak openings, missing metadata, brittle cleanup scripts, or outputs that fail a quick preach/read test. Keep changes small and traceable, update the affected `SKILL.md` and local assets together, and validate against at least one realistic case before release.

## Checklist before publishing

Before publishing or asking users to update installed skills:

- Each skill directory under `skills/` has a `SKILL.md`.
- Each `SKILL.md` starts with valid YAML frontmatter.
- Frontmatter `name` matches the directory name.
- Frontmatter `description` explains both what the skill does and when to use it.
- `skills.json`, if kept, lists every skill directory and no missing/renamed skill.
- Human docs under `docs/` link to `docs/skills/*.md`.
- New templates or scripts live inside the owning skill directory.
- Reusable skill content does not depend on local absolute paths, private repos, or machine-specific names.
- Install smoke for the intended target agents is done with `bunx skills add ...` before release.

See the full publishing and update checklist in [`docs/distribution.md`](docs/distribution.md).

## Documentation

[`docs/`](docs/) — human usage guides. Skill-specific notes live under [`docs/skills/`](docs/skills/).

## How to use

Each skill is invoked with `/teo-<name>`:

```text
/teo-sermao
/teo-sermao --estilo=emilio
/teo-transcricao
/teo-debate
/teo-livro
```
