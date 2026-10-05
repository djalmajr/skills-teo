# Convenções

## Estrutura

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
    ├── teo-debate/
    │   ├── SKILL.md
    │   ├── examples/
    │   ├── references/
    │   └── templates/
    ├── teo-livro/
    │   ├── SKILL.md
    │   ├── references/
    │   └── templates/
    ├── teo-sermao/
    │   ├── SKILL.md
    │   ├── references/
    │   └── estilos/
    └── teo-transcricao/
        ├── SKILL.md
        └── scripts/
```

## SKILL.md

- Comece com metadados YAML contendo pelo menos `name` e `description`.
- `name` deve ser igual ao nome do diretório e usar o prefixo `teo-`.
- Escreva o procedimento para que um agente possa executá-lo sem contexto privado.
- Prefira caminhos relativos dentro do diretório da skill.
- Mantenha os gatilhos em `description` (o que faz + quando usar).

## Idioma

- Todo texto visível das skills e da documentação deve estar em português do Brasil (pt-BR). Inglês só pode permanecer em nomes próprios, comandos, campos YAML, caminhos e identificadores técnicos.
- A documentação de instalação/distribuição e os corpos das skills deste repositório seguem o mesmo padrão pt-BR.

## Formatação

- Mantenha cada parágrafo e item de lista em uma única linha, sem quebras manuais para limitar a largura.
- Preserve quebras estruturais em blocos de código, tabelas, listas, metadados YAML e versos.

## Autossuficiência

Uma skill não pode exigir:

- caminhos absolutos como `/Users/...`
- coleções pessoais de notas ou árvores do OneDrive
- segredos, tokens ou chaves de API privadas
- coleções locais não documentadas

Se um fluxo precisar de uma pasta de destino, use a pasta informada pela pessoa usuária ou o diretório de trabalho atual.

## Produtos de trabalho gerados

`teo-transcricao` cria pastas de coleção (`raw/`, `artigos/`). `teo-debate` cria `indice.md` + `raw/` (protocolo, turnos, síntese, veredito). `teo-livro` cria `indice.md` + `livro/` (AsciiDoc) + `raw/` (pesquisa, plano de capítulos, edição) em uma pasta **separada** de qualquer debate. Esses itens pertencem ao diretório de trabalho da pessoa usuária, não ao pacote da skill. Uma pasta de debate é autossuficiente: não cita uma nota preexistente de uma coleção pessoal como fonte e não contém o livro.

## Exemplos e transcrições

- `examples/` = cartões estruturais curtos para calibração
- `transcriptions/` = prosa editorial mais longa para calibração de voz/ritmo
- Ambos são materiais de referência, não conteúdo para colar integralmente em sermões novos
- Em `teo-sermao`, ficam sob o estilo que os utiliza (`estilos/emilio/examples/`, `estilos/emilio/transcriptions/`)

## Verificação

```bash
npm test
```

O comando confirma:

1. cada diretório `skills/*` tem `SKILL.md`
2. o `name` do bloco de metadados corresponde ao diretório
3. `skills.json` lista exatamente essas skills
