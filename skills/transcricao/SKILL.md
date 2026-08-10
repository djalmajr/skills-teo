---
name: transcricao
description: >-
  Pipeline completo para transformar vídeos/playlists do YouTube (sermões, exposições
  bíblicas, aulas teológicas, lives pastorais) em artigos em prosa: baixa legendas com
  yt-dlp, limpa eco de auto-legenda (rolling ASR), reescreve em Markdown publicado e
  organiza raw/ + artigos/. Use sempre que o usuário pedir transcrição de pregação,
  legenda de sermão, "passa esse YouTube pra texto", playlist de exposições, artigo a
  partir de vídeo teológico, limpar SRT/VTT, remover vícios de oralidade de legenda,
  ou montar coleção de notas a partir de vídeos — mesmo sem dizer "transcrição".
---

# Transcrição → Artigo

Transforme URL(s) do YouTube em **artigos legíveis**, com material bruto preservado para auditoria.

Não entregue estenotipia com timestamps. O artefato final é prosa editorial fiel ao sentido da exposição.

Esta skill é **autossuficiente**: o fluxo e o script de limpeza estão aqui. Não dependa de documentos externos da coleção do usuário. Não use caminhos, nomes de máquina, pastas pessoais ou coleções de exemplo de ninguém.

## Quando usar

- Transcrever sermão / exposição / aula / palestra do YouTube
- Processar playlist ou lote de URLs
- Limpar `.srt`/`.vtt` com eco de auto-legenda
- Reescrever oralidade em artigo com parágrafos e pontuação
- Organizar coleção `raw/` + `artigos/` + índice

## Quando NÃO usar

- Criar sermão ou texto novo do zero (sem base em áudio/vídeo)
- Exegese técnica desconectada de uma fonte falada
- Download do vídeo em si (esta skill baixa **só legendas**, salvo pedido explícito em contrário)
- Legenda palavra-por-palavra com timestamps para legendagem de vídeo

## Pré-requisitos

- `yt-dlp` no PATH (instalar/atualizar se o extractor falhar ou houver 429)
- Python 3
- Rede para o YouTube

```bash
which yt-dlp && yt-dlp --version
python3 --version
```

## Localizar o script da skill

```text
transcricao/
├── SKILL.md
└── scripts/
    └── limpar_legendas.py
```

Resolva o caminho a partir do diretório desta skill (como o agente a carregou):

```bash
python3 "$SKILL_DIR/scripts/limpar_legendas.py" --help
```

Não hardcode caminhos de máquina. Use a **pasta de destino** informada pelo usuário (ou o cwd).

## Saída padrão (pasta da coleção)

```text
<colecao>/
├── README.md
├── artigos/                    # prosa final
│   ├── 01-slug-do-titulo.md
│   └── ...
└── raw/
    ├── legendas-brutas/        # .srt / .vtt
    └── textos-limpos/          # texto corrido oral, sem timestamps
```

Convenções:

- Numeração `01`, `02`, … na ordem da coleção
- Texto limpo: `NN - [Autor] ｜ [Título] ｜ [VIDEO_ID].txt`
- Artigo: `NN-slug-do-titulo.md`
- Preserve sempre os brutos em `raw/`
- Não sobrescreva artigo já editado à mão sem backup ou confirmação

## Pipeline (ordem fixa)

```text
URL(s)
  → 1. Metadados
  → 2. Legendas (yt-dlp)
  → 3. Texto limpo (script desta skill)
  → 4. Artigo(s) Markdown com bloco de metadados
  → 5. QA + README da coleção
```

Não pule para o artigo sem texto limpo. Não apague legendas brutas depois de limpar.

---

### 1) Metadados

Para cada URL (ou itens de playlist), colete campos ricos — eles vão para o artigo:

```bash
yt-dlp --skip-download --flat-playlist \
  --print "%(playlist_index)s|%(id)s|%(title)s|%(channel)s|%(uploader)s|%(upload_date)s|%(duration)s|%(webpage_url)s|%(playlist_title)s|%(playlist_id)s" \
  "URL_OU_PLAYLIST"
```

Campos a capturar:

| Campo | Origem típica | Obrigatório no artigo? |
|---|---|---|
| `url` | `webpage_url` | **sim** |
| `id` | id do vídeo | sim (rastreio / nome de arquivo) |
| `title` | título do vídeo | sim |
| `author` / pregador | título, canal, descrição ou usuário | **sim** |
| `channel` | canal do YouTube | recomendado |
| `date` / `upload_date` | `YYYYMMDD` → `YYYY-MM-DD` | recomendado |
| `duration` | segundos → legível (`45 min`) | opcional |
| `series` / playlist | título da playlist, se houver | opcional |
| `passage` / tema | título ou conteúdo | opcional |
| `NN` | próximo índice livre na coleção | sim na coleção |

Se a playlist misturar autores, grave a autoria correta em cada item. **Não invente** autor, data ou URL.

---

### 2) Baixar legendas

Só legendas — não o vídeo:

```bash
mkdir -p raw/legendas-brutas raw/textos-limpos artigos

yt-dlp \
  --skip-download \
  --write-auto-subs \
  --write-subs \
  --sub-langs "pt,pt-BR,pt-PT,en,en-US,en-GB" \
  --convert-subs srt \
  --sleep-requests 1 \
  --sleep-interval 1 \
  --max-sleep-interval 3 \
  -o "raw/legendas-brutas/%(id)s - %(title)s" \
  "URL_1" "URL_2"
```

Ajuste `--sub-langs` se o usuário pedir outro idioma. Prioridade default na limpeza: `pt` > `pt-BR` > `pt-PT` > `en` > `en-US` > `en-GB`.

Problemas comuns:

| Sintoma | Ação |
|---|---|
| HTTP 429 | pausar; rerodar só o ID faltante; manter sleeps |
| ficou `.vtt` | ok — o script lê srt e vtt |
| sem legenda no idioma preferido | use o melhor fallback; o texto do artigo já revela o idioma |
| warning de impersonation | ignorável se o arquivo baixou |
| vídeo sem legenda | informe o usuário; não invente o monólogo |

---

### 3) Texto limpo (dedupe rolling ASR)

Auto-legendas do YouTube **repetem o fim do cue anterior** em cada linha nova. Sem merge, o texto fica ilegível.

```bash
python3 "$SKILL_DIR/scripts/limpar_legendas.py" \
  --input-dir "raw/legendas-brutas" \
  --output-dir "raw/textos-limpos" \
  --id VIDEO_ID \
  --num 07 \
  --title "Título do vídeo" \
  --preacher "Nome do autor" \
  --url "https://..."
```

Lote (manifesto JSON = lista de objetos com `id`, `n`, `title`, `preacher`, `url`):

```bash
python3 "$SKILL_DIR/scripts/limpar_legendas.py" \
  --input-dir "raw/legendas-brutas" \
  --output-dir "raw/textos-limpos" \
  --manifest "raw/novos-videos.json"
```

O script: escolhe idioma → remove timestamps/tags → merge rolling → parágrafos → `.txt` com header de origem.

**Checagem antes de seguir:** início sem eco; palavras na ordem de grandeza da duração; idioma legível no próprio texto.

O texto limpo ainda é **oral**. A prosa final fica no passo 4.

---

### 4) Reescrever como artigo

Um arquivo por exposição. Em lotes, paralelize (uma tarefa por vídeo).

#### Formato obrigatório do artigo

Todo artigo começa com **título + bloco de metadados** e só então o corpo. Use YAML frontmatter (preferido) **ou** bloco Markdown equivalente — mas seja consistente na coleção.

**Preferido (YAML frontmatter):**

```markdown
---
title: "Título do artigo"
author: "Nome do autor/pregador"
source: "https://www.youtube.com/watch?v=VIDEO_ID"
video_id: "VIDEO_ID"
date: "YYYY-MM-DD"
channel: "Nome do canal"
duration: "46 min"
series: "Nome da série ou playlist, se houver"
passage: "Referência bíblica ou tema, se houver"
---

# Título do artigo

Introdução em prosa…

## Seção temática

Parágrafos…

## Conclusão

…
```

Regras do bloco de metadados:

1. **`source` (URL) é obrigatório** quando a fonte for um vídeo/URL conhecido.
2. **`author` é obrigatório.**
3. Inclua `date`, `channel`, `video_id`, `duration`, `series`, `passage` quando disponíveis.
4. **Não inclua idioma da legenda** — o texto do artigo já revela o idioma.
5. **Não inclua** caminhos locais, nome de arquivos `.srt`, nem confissão de “auto-legenda” no corpo.
6. Omita campos desconhecidos; não invente.
7. `date` em ISO `YYYY-MM-DD` quando vier de `upload_date`.
8. `duration` legível (`45 min`) a partir dos segundos do yt-dlp.
9. Crédito final opcional e discreto: `*Baseado na exposição de [Autor].*` — sem repetir a URL se ela já está nos metadados.

#### Regras editoriais do corpo

1. **Preserve substância e ordem das ideias.** Não invente doutrina, exemplos ou aplicações ausentes do original.
2. **Não resuma demais.** Corte só repetição, hesitação e enrolação de palco/live.
3. **Prosa publicada:** pontuação, capitalização, parágrafos curtos/médios.
4. **Remova vícios de oralidade** da língua do áudio (em pt-BR: né, tá, tipo, assim, aí, beleza, olha só, ééé, etc.) — exceto citação intencional.
5. **Ilustrações:** mantenha se carregam o argumento; enxugue se só aquecem o público.
6. **Corrija ASR óbvio** com contexto. Se incerto, formulação prudente ou omissão — **não chute**.
7. **Autoria correta** nos metadados (coleções mistas existem).
8. Sem timestamps no corpo.
9. Nome do arquivo: `NN-slug-ascii-com-hifens.md`.

#### Critérios de pronto

- [ ] Frontmatter/metadados com pelo menos `title`, `author`, `source`
- [ ] Lê como artigo, não como legenda
- [ ] Seções `##` naturais ao movimento da exposição
- [ ] Quase zero tiques orais
- [ ] Nomes/lugares revisados
- [ ] Brutos intactos em `raw/`

Estimativa: ~45–50 min de fala → artigo de ~4–6k palavras se a substância for preservada.

---

### 5) QA e índice

```bash
rg -n -i --pcre2 '\b(né|tá bom|beleza|tipo assim|microfone|ééé|olha só)\b' artigos/
# metadados presentes?
rg -L -n '^source:|^author:' artigos/*.md || true
wc -w artigos/*.md
```

Atualize o `README.md` da coleção com fontes, lista de artigos (título, autor, ~palavras) e nota de que a base é legenda + edição editorial.

## Defaults

| Situação | Default |
|---|---|
| Pasta não dita | coleção no cwd com o layout acima |
| Idioma do artigo | o do usuário / o do áudio |
| Legenda | preferir `pt*`, senão melhor fallback |
| Numeração | continuar do maior `NN` existente |
| Lote | um artigo por vídeo |
| Vídeo sem legenda | informar; não inventar |
| Metadados | URL + autor sempre; demais campos quando existirem |

## Entrada mínima

| Campo | Obrigatório? | Notas |
|---|---|---|
| URL(s) ou playlist | sim | |
| Pasta destino | recomendado | senão cwd |
| Autor | recomendado | inferir do título/canal com cautela |
| Numeração | opcional | auto se já houver coleção |
| Só raw / só artigo | opcional | default = pipeline completo |

## Limitações

- Auto-legenda erra nomes, referências e termos raros
- O merge rolling remove eco; não interpreta o conteúdo
- O artigo é **edição fiel ao sentido**, não certidão palavra-por-palavra
- Para uso público/formal sensível, recomende checagem de ouvido nos trechos críticos

## Anti-padrões

- Entregar SRT/VTT como “transcrição final”
- Artigo sem URL/`source` quando a fonte é um vídeo conhecido
- Incluir “idioma da legenda” nos metadados do artigo
- Apagar `raw/` depois de gerar o artigo
- Resumir fala longa sem o usuário pedir resumo
- Homogeneizar autoria quando há vários expositores
- Inventar pontes ou aplicações ausentes do áudio
- Baixar o vídeo completo sem necessidade
- Depender de arquivos pessoais ou docs fora desta skill

## Escopo

Esta skill cobre **captura + limpeza + edição editorial** de exposição existente.  
Não substitui skill de **criação** de sermão/texto novo.
