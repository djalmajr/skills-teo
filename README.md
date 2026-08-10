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
bunx skills add djalmajr/skills-teo --skill sermao-emilio
bunx skills add djalmajr/skills-teo --skill transcricao

# Explicit target agents
bunx skills add djalmajr/skills-teo --agent claude-code --agent opencode --agent codex --skill '*'
```

## Package layout

This repo follows the shared Agent Skills convention:

```text
skills/<skill-name>/SKILL.md          # project-authored, distributed skills
skills/<skill-name>/scripts/          # optional helpers owned by the skill
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

## Skills (2)

| Skill | Purpose |
|-------|---------|
| sermao-emilio | Cria sermões no padrão narrativo-pastoral (história do cotidiano, costuras no meio, 2–3 partes, graça no fecho) |
| transcricao | Pipeline YouTube → legendas → texto limpo → artigo em prosa; organiza `raw/` + `artigos/` |

## Flow

```text
fonte (texto bíblico ou URL)
  → skill de criação (sermao-emilio)
    ou captura/edição (transcricao)
  → artefato pregável / artigo
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

Each skill is invoked with `/skill-name`:

```text
/sermao-emilio
/transcricao
```
