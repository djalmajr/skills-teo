---
name: debate
description: >-
  Media um debate entre três agentes independentes. Antes de lançar, monta o
  tema com perguntas estruturadas (não parte de uma nota de vault). Julga a
  qualidade de cada turno (com retrabalho se a peça falhar) e fecha com mapa
  + veredito: o que a tese deste debate sobreviveu, não um placar de escolas
  — salvo o usuário pedir juízo doutrinário. Use quando pedir debate,
  disputa escatológica, amilenarismo vs pré-milenarismo vs
  dispensacionalismo, tribunal, mediador no Herdr, "três posições sobre",
  ata+síntese+veredito. Também /teo-debate.
  Não escreve livro: isso é a skill `livro`, opcional, depois.
---

# Debate

Media **três proponentes** em sessões independentes. Você é o **mediador**: entrevista o tema, define o elenco, impõe turnos cegos, **julga a qualidade de cada peça**, manda retrabalho se falhar, e fecha com mapa + veredito sobre a tese **deste** debate.

Os panes/terminais **não** são arquivo. Se não estiver na `sintese.md`, na `atas.md` ou no `veredito.md`, não aconteceu.

## Quando usar

- Disputa entre escolas (escatologia, soteriologia, batismo, dons, etc.)
- Testar uma tese (nascida neste debate) contra três leituras rivais
- Rodar três agentes no Herdr e mediar o cruzamento
- Documentar um debate para estudo posterior (ata + síntese + veredito) — não o livro

## Quando NÃO usar

- Escrever sermão ou artigo de uma só voz (`sermao`)
- Transcrever exposição existente (`transcricao`)
- Escrever um livro ou ebook (`livro`) — mesmo que o insumo venha a ser este debate
- Exegese de um único texto sem confronto de escolas
- "Debate" com um só agente mudando de chapéu (isso contamina)

## Princípios

1. **Três posições que discordam da pergunta real**, não três rótulos que secretamente concordam.
2. **Mesmo modelo / mesmo `kind`** nos três agentes. A variável é a doutrina, não o LLM.
3. **Turno cego e simultâneo.** Ninguém lê o outro antes de gravar a peça.
4. **Cânon no disco, no fim de cada turno** — nunca só no encerramento.
5. **Ata estruturada, não dump.** Preservar informação ≠ guardar cada token.
6. **Não crie a pasta nem lance agentes** até o intake estar completo e o usuário autorizar o lançamento.
7. **Agenda compartilhada.** Todo T01 preenche os mesmos eixos, na mesma ordem. Sem isso o quadro não compara.
8. **T01 trava.** Depois de gravado em `turnos/`, o ensaio de abertura não se edita. Réplica responde à peça entregue.
9. **Três camadas de juízo, não uma.** Mapa (síntese) ≠ qualidade (gate) ≠ veredito. Não declare vencedor de escola por default. Sempre declare: (a) a qualidade do turno, (b) o que a tese deste debate ainda pode afirmar. Juízo doutrinário só se o usuário pedir.
10. **Auto-contido.** Tema, pergunta e tese nascem no intake e moram no protocolo. Índice e briefs não citam nota, artigo ou path fora da pasta.
11. **O debate é o produto.** Síntese + veredito + turnos. Não compile volume aqui. Livro, se o usuário quiser, é a skill `livro`, outra pasta, outro ciclo.

Calibração do protocolo: `references/metodo-quatro-pontos.md` (Grudem, ed., *Cessaram os dons espirituais?*). Copie o método, não o tema.

## Intake (antes de criar pasta ou lançar)

O debate **não** começa numa nota de vault. Rode `references/intake.md` com a ferramenta de pergunta estruturada (`ask_user_question` / `AskUserQuestion` / `question`). Sem as respostas, pare.

| Campo | Obrigatório? | Default |
|---|---|---|
| Tema (uma frase, não um path) | sim | — |
| Pergunta real | sim | — |
| Tese deste debate (prosa, 3–6 frases) | sim | — |
| Elenco | sim (confirmar) | catálogo `escatologia-milenio` se o tema for escatologia |
| Fora do tribunal | sim | caricaturas do elenco, se o usuário aceitar |
| Idioma de saída | sim (confirmar) | português do Brasil |
| Pasta destino | sim | `Debate - <tema>/` no cwd |
| Autorização para lançar | sim | — |
| Runtime | implícito | Herdr se `HERDR_ENV=1`; senão modo degradado |
| Kind dos agentes | opcional | o mesmo kind do mediador |

Leia `references/elencos.md` **depois** do intake, para nomear ids. Não misture dispensacionalismo clássico com o progressivo, nem pré-milenarismo histórico com o pop de relógio de noticiário.

Se duas escolas dão a **mesma resposta à pergunta real**, funda-as num assento (Grudem fundiu pentecostal + carismático para não desequilibrar o tabuleiro). Não invente um quarto agente “aberto porém cauteloso” a menos que seja tese própria, com representantes.

## Artefatos (pasta do usuário)

Crie isto **antes** de lançar agentes. Não grave debate dentro desta skill.

```text
<destino>/
├── indice.md            # porta: tema, pergunta, vozes; aponta síntese + veredito + turnos
└── raw/                 # protocolo, briefs, turnos, atas, qualidade, síntese, veredito, curadoria
```

Copie a ossatura de `templates/` (`indice.md`, `00-protocolo.md`, `brief.md`, …). Preencha com as respostas do intake; não deixe placeholder. Destino = pasta que o usuário pediu, senão cwd. Sem caminhos absolutos de máquina.

A tese deste debate vive no protocolo. Não aponte agentes para arquivo fora da pasta.

## Runtime

### Herdr (protocolo completo)

Só controle a sessão se `test "${HERDR_ENV:-}" = 1`. Se falhar, não inspecione a sessão alheia.

1. Confirme kind: `herdr agent` (o mediador deve usar o mesmo `--kind` nos três).
2. Crie a pasta destino a partir de `templates/` (`indice.md`, `00-protocolo.md`, `formato-turno.md`, `atas.md`, `sintese.md`, `qualidade.md`, `veredito.md`, `aprendizados.md`, `turnos/`, `briefs/<id>.md` a partir de `brief.md`).
3. Layout: mediador permanece no pane atual. Três agentes empilhados à direita, **sem roubar foco**, **mesmo cwd da pasta destino**:

```bash
herdr pane layout --pane "$HERDR_PANE_ID"

# coluna direita
herdr pane split --current --direction right --cwd "$DESTINO" --no-focus
# empilhar os outros dois no pane recém-criado (ID vem do JSON)
herdr pane split --pane <id-direita> --direction down --cwd "$DESTINO" --no-focus
herdr pane split --pane <id-inferior> --direction down --cwd "$DESTINO" --no-focus
```

Pane largo → primeira divisão `right`. Splits binários empilhados **não** ficam iguais: depois dos três splits, `herdr pane resize` até as alturas da coluna direita ficarem próximas. `--amount` é grosso; leia o layout depois de cada resize. Não invente IDs; leia o JSON. Não feche pane que você não criou. Não crie workspace/tab/worktree a menos que o usuário peça.

4. Em cada pane-irmão, no prompt do shell:

```bash
herdr agent start <nome> --kind <kind> --pane <pane-id>
```

`nome` ∈ `[a-z][a-z0-9_-]{0,31}`, único, igual ao id do elenco (`amilenarista`, `premilenarista`, `dispensacionalista`).

5. `herdr agent prompt` **sem** `--wait` (aponta o arquivo em disco; não cole o brief). `--wait` no Grok pode devolver `agent_prompt_stalled` aos 5s mesmo com o texto já na tela. Sem `--wait`, a resposta pode ainda dizer `done` com seq antiga: confira `herdr agent get` até `working`, depois `herdr agent wait <nome> --timeout 600000`. Não reenvie o prompt. Timeout folgado: T01 ~3–5 min em Grok xhigh; réplica ~2–3 min.

6. Peça a cada agente **um arquivo** `turnos/TNN-<nome>.md` no formato de `formato-turno.md`, e no chat só o path. Grok vive em tela alternativa: enquanto `working`, use `--source visible`; o cânon é o arquivo. Se o agente não gravar, extraia via `herdr agent read <nome> --source recent-unwrapped --lines 200` **depois de idle** e grave o arquivo você.

Comandos úteis: `herdr agent prompt`, `wait`, `read`, `get`. Não rode `herdr` nu (abre TUI).

### Sem Herdr (degradado)

Avise que não há sessões independentes. Não finja três vozes no mesmo contexto: o segundo já viu o primeiro.

Opções, nesta ordem:

1. Pedir para rodar dentro do Herdr.
2. Se o usuário insistir: três *subagentes isolados* (worktrees/processos separados, sem histórico compartilhado), você só funde depois. Documente na `00-protocolo.md` que o runtime foi degradado.

Nunca faça os três papéis você mesmo no mesmo fio.

## Ciclo de um turno

```text
pauta → T01 cego → gate de qualidade (± retrabalho) → atas + síntese
  → réplica → gate (± correção de mal-entendido agora)
  → declaração final → mapa + veredito → curadoria do debate
```

1. **Pauta.** Uma pergunta, ou um feixe curto da tese deste debate. O mediador formula; os agentes não escolhem o tema do turno. T01 usa a **agenda compartilhada** do protocolo (os eixos do catálogo), não um ensaio livre.
2. **Cego.** Os três recebem a mesma pergunta e **não** recebem as peças alheias. Réplica só no turno seguinte, já com as peças anteriores citadas pelo mediador (não pelo próprio agente vasculhando a pasta dos outros — o brief deve proibir ler `turnos/` de outro nome).
3. **Trava + gravação.** T01 em `turnos/` fica imutável. Em `atas.md` não cole a peça inteira: path + tese + perigos + concessão + o que resta. O bruto já está em `turnos/`.
4. **Gate de qualidade.** Antes da síntese, preencha `qualidade.md` (template). Peça **RETRY** se a falha for das que mandam retrabalho; **WARN** vira pauta, não retrabalho. Máximo 2 retrabalhos por agente por turno. O prompt de retrabalho diz o motivo e manda regravar o **mesmo** path; continua cego.
5. **Síntese.** Atualize `sintese.md` inteira: acordo, glossário, quadro, discordância-mestra, índice, implicação, abertos. Só peças PASS (ou WARN após esgotar retrabalho).
6. **Réplica.** Curta. Steelmán do mediador (5–8 linhas), não o arquivo inteiro. Recusa pontual. Se a réplica atacar o que o outro **não** sustentou, **corrija agora** (pauta de mal-entendido, 1 pergunta) — não deixe isso para a declaração final.
7. **Declaração final.** `turnos/TF-<id>.md`. Aceita as mestras? o que agora entende do outro? o que ainda sustenta (≤3 teses)? Conferir mtime de todos os turnos anteriores.
8. **Veredito.** Grave `raw/veredito.md`. Sem isso o debate não fechou. Três camadas no template; a 3 só se o usuário pediu vencedor de escola.
9. **Não o livro.** Se o usuário pedir volume, ebook ou Four Views literário, **pare** e aponte a skill `livro`. Não rascunhe `livro/` nesta pasta. O dossiê da disputa é o produto.

Pauta padrão do catálogo `escatologia-milenio` (use a tese deste debate se ela já trouxer perguntas):

1. Satanás ainda tem jurisdição sobre a humanidade, ou só exerce usurpação?
2. Se o valente foi amarrado, por que a parábola do semeador ainda descreve o adversário tirando a palavra?
3. Como ficam os filhos do diabo se ele já perdeu o direito sobre a humanidade?
4. O reino davídico foi inaugurado ou adiado? A igreja herda Israel?

As perguntas 1–3 separam os três no *agora*. A 4 obriga os dois pré-milenaristas a brigarem entre si (evita 2 contra 1 no milênio literal).

## Brief de cada agente

No primeiro prompt, cada um recebe:

- quem é (escola, representantes, o que **não** é)
- tese **positiva** (o que defende, não só o que nega — rótulo anti-X não basta)
- **os outros neste tribunal** — uma linha cada, tirada da coluna “Não é” do elenco, para não caricaturar desde o T01
- regras do tribunal (abaixo)
- path de `00-protocolo.md` (a tese está lá; nada fora desta pasta)
- a pergunta do turno + eixos da agenda compartilhada
- ordem: gravar `turnos/TNN-<nome>.md` no formato de `templates/turno.md`

Regras que vão no brief (e no protocolo):

- Citar Escritura no fio (livro, capítulo e versículo junto da declaração; nomear o episódio não basta); distinguir cumprimento, andamento e resto
- Defender a **melhor** versão da própria escola, não a média popular
- Steelmán o outro antes de refutar (na réplica)
- Nomear **perigos da própria posição**, não só os do outro
- Proibido relógio de noticiário, anedota de leigo como refutação da escola, caricatura
- Não ler peças dos outros agentes até o mediador colar o steelman
- Não conceder o que a escola não concede só para parecer irênico
- Idioma do protocolo (default: português do Brasil); tom de advogado, não de influencer
- Teses da seção **Fora do tribunal** do protocolo: ninguém as defende nem as atribui ao outro
- Na réplica, recuse o **steelman do mediador**, não a caricatura. Se o steelman estiver errado, diga em uma linha e recuse o que o outro de fato sustentou

## Síntese (o documento de estudo)

Estrutura fixa — `templates/sintese.md`:

1. Acordo (o que os três já aceitam)
2. Glossário (mesmo fenômeno, nomes diferentes — não misture a briga de palavra com a de tese)
3. Quadro de teses (linhas = eixos da agenda; colunas = os três)
4. Discordância-mestra (a pergunta que, se resolvida, arrasta as outras)
5. Índice de textos (referência → quem usou → a favor de quê)
6. Implicação eclesial (o que mudaria na igreja / na piedade se cada tese vencesse)
7. Concessões e perigos próprios admitidos
8. Perguntas em aberto (viram o próximo turno)
9. Nota de turno (N, data, runtime)

Você lê a síntese (mapa) e o `veredito.md` (e daí). A ata existe para auditar uma frase. Não entregue paste dos três chats. Sem `veredito.md` o ciclo não fechou.

## Gate de qualidade (obrigatório a cada turno)

Template: `templates/qualidade.md` → `qualidade.md` no destino.

O mediador lê as três peças **antes** de atualizar a síntese. Não é opinião: é checklist.

RETRY (regrava o mesmo arquivo, cego, motivo no prompt):

- saiu da escola / defendeu a caricatura de si
- não percorreu a pauta
- atribuiu tese da lista Fora do tribunal
- arquivo ausente ou fora do formato
- editou turno anterior travado
- citação de carga cujo texto não diz o que a peça afirma (versículo errado ou inventado)

WARN (não retrabalha; anota e vira pauta se preciso):

- um eixo em branco
- texto decisivo só um lado citou
- steelman um pouco torto, sem caricatura
- citação de apoio frouxa; alusão sem versículo

Leitura da escola sobre um texto que *está* ali não é erro de fonte.

Mal-entendido (atacar o que o outro não sustentou): pauta curta **neste ciclo**, não na declaração final. A declaração final confirma o ouvido; não é a primeira correção.

Máximo 2 RETRY por agente por turno. Se ainda falhar: WARN na síntese e segue. Não troque de modelo no retrabalho.

## Encerramento

Quando o quadro estabilizar ou o usuário pedir para fechar:

1. Última passagem na `sintese.md` (mapa). Sem perguntas órfãs.
2. Grave `raw/veredito.md` (`templates/veredito.md`): qualidade + o que a tese deste debate sobreviveu. Camada 3 só se o usuário pediu vencedor de escola.
3. Preencha `raw/aprendizados.md`.
4. `indice.md` na raiz: porta (tema, pergunta, vozes) + ordem de leitura do **debate** (protocolo → síntese → veredito → turnos).
5. **Curadoria do debate.** Grave `raw/curadoria.md` (`templates/curadoria.md`): referências batem, o protocolo foi cumprido. Sem isso o debate não fechou. Não é um quarto debatedor e não escolhe escola. Prefira um subagente isolado. `não` numa citação de carga → RETRY da peça (se ainda for turno) ou nota no veredito (se o turno já travou).
6. Patcheie a skill se o usuário pediu ajuste contínuo.
7. Livro **não** faz parte deste encerramento. Convite explícito, se couber: «o dossiê está fechado; volume é `/teo-livro`, outra pasta.»

## Anti-padrões

- Lançar agentes (ou criar a pasta) antes do intake
- Apontar índice, brief ou agentes para nota, artigo ou path fora da pasta
- Misturar kinds/modelos
- Deixar o segundo agente ver o primeiro no mesmo turno
- Confiar em scrollback do Herdr como arquivo
- Colar transcript inteiro como “resultado”
- Elenco em que dois secretamente concordam na pergunta real
- Dispensacionalismo progressivo no lugar do clássico (apaga o contraste com Ladd)
- Pré-milenarismo de YouTube (arrebatamento secreto como eixo único)
- Preterismo completo num trio escatológico (muda a pergunta para “ainda existe escatologia?”)
- Você mesmo interpretar os três papéis
- Mediador tomar escola no mérito **sem** o usuário ter pedido juízo doutrinário
- Criticar a escola com anedota de leigo
- Deixar T01 ser reescrito depois da réplica
- Tratar briga de vocabulário como se fosse briga de tese
- Fechar só com mapa (“e daí?” sem `veredito.md`)
- Entregar o debate sem `raw/curadoria.md`
- Tratar leitura da escola como erro de citação — ou o inverso, erro de citação como “é a leitura”
- Compilar livro, ebook ou `livro/` no encerramento desta skill (aponta `livro`)
- Aludir a um texto ou episódio bíblico sem capítulo e versículo
- Deixar mal-entendido viver até a declaração final
- Declarar vencedor de escola por default
- Vocabulário de outro português nas peças quando o idioma for pt-BR (ficheiro, ecrã, de facto)

## Checklist antes de lançar

- [ ] Intake via pergunta estruturada (tema, pergunta, tese em prosa, elenco, fora, idioma, destino, autorização)
- [ ] Tese deste debate no protocolo, sem path externo
- [ ] `indice.md` auto-contido (tema, pergunta, vozes)
- [ ] Elenco confirmado; os três discordam da pergunta
- [ ] Pasta destino criada com protocolo (agenda + fora do tribunal) + atas + síntese vazia
- [ ] Usuário disse para lançar
- [ ] `HERDR_ENV=1` (ou modo degradado declarado)
- [ ] Mesmo `--kind` nos três
- [ ] Nomes Herdr-safe
- [ ] cwd dos panes = pasta destino
- [ ] Foco permanece no mediador

## Checklist no fim de cada turno

- [ ] Três arquivos em `turnos/TNN-*` (ou `TF-*`)
- [ ] `qualidade.md` preenchido; RETRY esgotado ou PASS
- [ ] Mal-entendido corrigido neste ciclo, se houve
- [ ] `atas.md` recebeu o turno
- [ ] `sintese.md` atualizada
- [ ] Turnos anteriores intocados (mtime)
- [ ] Próxima pauta sai dos abertos, da mestra ou de um WARN — não de tema novo
- [ ] Se fechou: `raw/veredito.md` e `raw/curadoria.md` existem; `indice.md` aponta o debate, não um volume
- [ ] Toda declaração bíblica de carga nas peças foi conferida (o texto diz o que a frase afirma)
