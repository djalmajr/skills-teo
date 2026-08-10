# Conventions

## Layout

```text
skills-teo/
├── README.md
├── package.json
├── skills.json
├── docs/
│   ├── README.md
│   ├── conventions.md
│   ├── distribution.md
│   └── skills/
└── skills/
    ├── sermao-emilio/
    │   ├── SKILL.md
    │   ├── examples/
    │   └── transcriptions/
    └── transcricao/
        ├── SKILL.md
        └── scripts/
```

## SKILL.md

- Start with YAML frontmatter containing at least `name` and `description`.
- `name` must equal the directory name.
- Write the procedure so an agent can run it without private context.
- Prefer relative paths inside the skill directory.
- Keep triggers in `description` (what + when).

## Language

- Skills may be authored in Portuguese when the domain is pastoral/theological for pt-BR users.
- Keep install/distribution docs bilingual-friendly; English package framing is fine at the root, Portuguese skill bodies are expected for this repo.

## Self-containment

A skill must not require:

- absolute paths like `/Users/...`
- personal note vaults or OneDrive trees
- secrets, tokens, or private API keys
- undocumented local collections

If a workflow needs a destination folder, take it from the user or use the current working directory.

## Generated work products

`transcricao` creates collection folders (`raw/`, `artigos/`). Those belong to the user's working directory, not to the skill package. Keep them out of this repository unless they are intentional public samples.

## Examples and transcriptions

- `examples/` = short structural cards for calibration
- `transcriptions/` = longer editorial prose for voice/rhythm calibration
- Both are reference material, not content to paste wholesale into new sermons

## Validation

```bash
npm test
```

The check confirms:

1. every `skills/*` directory has `SKILL.md`
2. frontmatter `name` matches the directory
3. `skills.json` lists exactly those skills
