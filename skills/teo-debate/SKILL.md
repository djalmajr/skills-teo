---
name: teo-debate
description: >-
  Media um debate entre três agentes independentes. Antes de lançar, monta o tema com perguntas estruturadas (não parte de uma coleção de notas). Julga a qualidade de cada turno (com retrabalho se a peça falhar) e fecha com mapa + veredito: o que a tese deste debate sobreviveu, não um placar de escolas — salvo o usuário pedir juízo doutrinário. Use quando pedir debate, disputa escatológica, amilenarismo vs pré-milenarismo vs dispensacionalismo, tribunal, mediador no Herdr, "três posições sobre", ata+síntese+veredito. Também /teo-debate. Não escreve livro: isso é a skill `teo-livro`, opcional, depois.
---

# Debate

Media **três proponentes** em sessões independentes. Você é o **mediador**: entrevista o tema, define o elenco, impõe turnos cegos, **julga a qualidade de cada peça**, manda retrabalho se falhar, e fecha com mapa + veredito sobre a tese **deste** debate.

Os painéis/terminais **não** são arquivo. Se não estiver na `sintese.md`, na `atas.md` ou no `veredito.md`, não aconteceu.

## Quando usar

- Disputa entre escolas (escatologia, soteriologia, batismo, dons, etc.)
- Testar uma tese (nascida neste debate) contra três leituras rivais
- Rodar três agentes no Herdr e mediar o cruzamento
- Documentar um debate para estudo posterior (ata + síntese + veredito) — não o livro

## Quando NÃO usar

- Escrever sermão ou artigo de uma só voz (`teo-sermao`)
- Transcrever exposição existente (`teo-transcricao`)
- Escrever um livro ou livro digital (`teo-livro`) — mesmo que o insumo venha a ser este debate
- Exegese de um único texto sem confronto de escolas
- "Debate" com um só agente mudando de chapéu (isso contamina)

## Princípios

1. **Três posições que discordam da pergunta real**, não três rótulos que secretamente concordam.
2. **Mesmo modelo / mesmo `kind`** nos três agentes. A variável é a doutrina, não o LLM.
3. **Turno cego e simultâneo.** Ninguém lê o outro antes de gravar a peça.
4. **Cânon no disco, no fim de cada turno** — nunca só no encerramento.
5. **Ata estruturada, não despejo.** Preservar informação ≠ guardar cada token.
6. **Não crie a pasta nem lance agentes** até a entrevista inicial estar completa e o usuário autorizar o lançamento.
7. **Agenda compartilhada.** Todo T01 preenche os mesmos eixos, na mesma ordem. Sem isso o quadro não compara.
8. **T01 trava.** Depois de gravado em `turnos/`, o ensaio de abertura não se edita. Réplica responde à peça entregue.
9. **Três camadas de juízo, não uma.** Mapa (síntese) ≠ qualidade (verificação) ≠ veredito. Não declare vencedor de escola por padrão. Sempre declare: (a) a qualidade do turno, (b) o que a tese deste debate ainda pode afirmar. Juízo doutrinário só se o usuário pedir.
10. **Auto-contido.** Tema, pergunta e tese nascem na entrevista inicial e moram no protocolo. Índice e orientações não citam nota, artigo ou caminho fora da pasta.
11. **O debate é o produto.** Síntese + veredito + turnos. Não compile volume aqui. Livro, se o usuário quiser, é a skill `teo-livro`, outra pasta, outro ciclo.

Calibração do protocolo: `references/metodo-quatro-pontos.md` (Grudem, ed., *Cessaram os dons espirituais?*). Copie o método, não o tema.

## Entrevista inicial (antes de criar pasta ou lançar)

O debate **não** começa em uma nota preexistente de uma coleção pessoal. Rode `references/intake.md` com a ferramenta de pergunta estruturada (`ask_user_question` / `AskUserQuestion` / `question`). Sem as respostas, pare.

| Campo | Obrigatório? | Padrão |
|---|---|---|
| Tema (uma frase, não um caminho) | sim | — |
| Pergunta real | sim | — |
| Tese deste debate (prosa, 3–6 frases) | sim | — |
| Elenco | sim (confirmar) | catálogo `escatologia-milenio` se o tema for escatologia |
| Fora do tribunal | sim | caricaturas do elenco, se o usuário aceitar |
| Idioma de saída | sim (confirmar) | português do Brasil |
| Pasta destino | sim | `Debate - <tema>/` no cwd |
| Autorização para lançar | sim | — |
| Ambiente de execução | implícito | Herdr se `HERDR_ENV=1`; senão modo degradado |
| Kind dos agentes | opcional | o mesmo kind do mediador |

Leia `references/elencos.md` **depois** da entrevista inicial, para nomear ids. Não misture dispensacionalismo clássico com o progressivo, nem pré-milenarismo histórico com o popular de relógio de noticiário.

Se duas escolas dão a **mesma resposta à pergunta real**, funda-as num assento (Grudem fundiu pentecostal + carismático para não desequilibrar o tabuleiro). Não invente um quarto agente “aberto porém cauteloso” a menos que seja tese própria, com representantes.

## Artefatos (pasta do usuário)

Crie isto **antes** de lançar agentes. Não grave debate dentro desta skill.

```text
<destino>/
├── indice.md            # porta: tema, pergunta, vozes; aponta síntese + veredito + turnos
└── raw/                 # protocolo, briefs, turnos, atas, qualidade, síntese, veredito, curadoria
```

Copie a ossatura de `templates/` (`indice.md`, `00-protocolo.md`, `brief.md`, …). Preencha com as respostas da entrevista inicial; não deixe marcadores provisórios. Destino = pasta que o usuário pediu, senão cwd. Sem caminhos absolutos de máquina.

A tese deste debate vive no protocolo. Não aponte agentes para arquivo fora da pasta.

## Ambiente de execução

### Herdr (protocolo completo)

Só controle a sessão se `test "${HERDR_ENV:-}" = 1`. Se falhar, não inspecione a sessão alheia.

1. Confirme kind: `herdr agent` (o mediador deve usar o mesmo `--kind` nos três).
2. Crie a pasta destino a partir de `templates/` (`indice.md`, `00-protocolo.md`, `formato-turno.md`, `atas.md`, `sintese.md`, `qualidade.md`, `veredito.md`, `aprendizados.md`, `turnos/`, `briefs/<id>.md` a partir de `brief.md`).
3. Disposição: mediador permanece no painel atual. Três agentes empilhados à direita, **sem roubar foco**, **mesmo cwd da pasta destino**:

```bash
herdr pane layout --pane "$HERDR_PANE_ID"

# coluna direita
herdr pane split --current --direction right --cwd "$DESTINO" --no-focus
# empilhar os outros dois no painel recém-criado (ID vem do JSON)
herdr pane split --pane <id-direita> --direction down --cwd "$DESTINO" --no-focus
herdr pane split --pane <id-inferior> --direction down --cwd "$DESTINO" --no-focus
```

Painel largo → primeira divisão `right`. Divisões binárias empilhadas **não** ficam iguais: depois das três divisões, `herdr pane resize` até as alturas da coluna direita ficarem próximas. `--amount` é grosso; leia a disposição depois de cada redimensionamento. Não invente IDs; leia o JSON. Não feche painel que você não criou. Não crie espaço de trabalho, aba ou worktree a menos que o usuário peça.

4. Em cada painel-irmão, na linha de comando do shell:

```bash
herdr agent start <nome> --kind <kind> --pane <pane-id>
```

`nome` ∈ `[a-z][a-z0-9_-]{0,31}`, único, igual ao id do elenco (`amilenarista`, `premilenarista`, `dispensacionalista`).

5. `herdr agent prompt` **sem** `--wait` (aponta o arquivo em disco; não cole a orientação). `--wait` no Grok pode devolver `agent_prompt_stalled` aos 5s mesmo com o texto já na tela. Sem `--wait`, a resposta pode ainda dizer `done` com seq antiga: confira `herdr agent get` até `working`, depois `herdr agent wait <nome> --timeout 600000`. Não reenvie a orientação. Prazo de espera folgado: T01 ~3–5 min em Grok xhigh; réplica ~2–3 min.

6. Peça a cada agente **um arquivo** `turnos/TNN-<nome>.md` no formato de `formato-turno.md`, e na conversa só o caminho. Grok vive em tela alternativa: enquanto `working`, use `--source visible`; o cânon é o arquivo. Se o agente não gravar, extraia via `herdr agent read <nome> --source recent-unwrapped --lines 200` **depois de idle** e grave o arquivo você.

Comandos úteis: `herdr agent prompt`, `wait`, `read`, `get`. Não rode `herdr` nu (abre TUI).

### Sem Herdr (degradado)

Avise que não há sessões independentes. Não finja três vozes no mesmo contexto: o segundo já viu o primeiro.

Opções, nesta ordem:

1. Pedir para rodar dentro do Herdr.
2. Se o usuário insistir: três *subagentes isolados* (worktrees/processos separados, sem histórico compartilhado), você só funde depois. Documente na `00-protocolo.md` que o ambiente de execução foi degradado.

Nunca faça os três papéis você mesmo no mesmo fio.

## Ciclo de um turno

```text
pauta → T01 cego → verificação de qualidade (± retrabalho) → atas + síntese
  → réplica → verificação (± correção de mal-entendido agora)
  → declaração final → mapa + veredito → curadoria do debate
```

1. **Pauta.** Uma pergunta, ou um feixe curto da tese deste debate. O mediador formula; os agentes não escolhem o tema do turno. T01 usa a **agenda compartilhada** do protocolo (os eixos do catálogo), não um ensaio livre.
2. **Cego.** Os três recebem a mesma pergunta e **não** recebem as peças alheias. Réplica só no turno seguinte, já com as peças anteriores citadas pelo mediador (não pelo próprio agente vasculhando a pasta dos outros — a orientação deve proibir ler `turnos/` de outro nome).
3. **Trava + gravação.** T01 em `turnos/` fica imutável. Em `atas.md` não cole a peça inteira: caminho + tese + perigos + concessão + o que resta. O bruto já está em `turnos/`.
4. **Verificação de qualidade.** Antes da síntese, preencha `qualidade.md` (modelo). Peça **RETRY** se a falha for das que mandam retrabalho; **WARN** vira pauta, não retrabalho. Máximo 2 retrabalhos por agente por turno. A orientação de retrabalho diz o motivo e manda regravar o **mesmo** caminho; continua cego.
5. **Síntese.** Atualize `sintese.md` inteira: acordo, glossário, quadro, discordância-mestra, índice, implicação, abertos. Só peças PASS (ou WARN após esgotar retrabalho).
6. **Réplica.** Curta. Apresente a versão mais forte do mediador (5–8 linhas), não o arquivo inteiro. Faça uma recusa pontual. Se a réplica atacar o que o outro **não** sustentou, **corrija agora** (pauta de mal-entendido, 1 pergunta) — não deixe isso para a declaração final.
7. **Declaração final.** `turnos/TF-<id>.md`. Aceita as mestras? o que agora entende do outro? o que ainda sustenta (≤3 teses)? Conferir mtime de todos os turnos anteriores.
8. **Veredito.** Grave `raw/veredito.md`. Sem isso o debate não fechou. Três camadas no modelo; a 3 só se o usuário pediu vencedor de escola.
9. **Não o livro.** Se o usuário pedir volume, livro digital ou Four Views literário, **pare** e aponte a skill `teo-livro`. Não rascunhe `livro/` nesta pasta. O dossiê da disputa é o produto.

Pauta padrão do catálogo `escatologia-milenio` (use a tese deste debate se ela já trouxer perguntas):

1. Satanás ainda tem jurisdição sobre a humanidade, ou só exerce usurpação?
2. Se o valente foi amarrado, por que a parábola do semeador ainda descreve o adversário tirando a palavra?
3. Como ficam os filhos do diabo se ele já perdeu o direito sobre a humanidade?
4. O reino davídico foi inaugurado ou adiado? A igreja herda Israel?

As perguntas 1–3 separam os três no *agora*. A 4 obriga os dois pré-milenaristas a brigarem entre si (evita 2 contra 1 no milênio literal).

## Orientação de cada agente

Na primeira orientação, cada um recebe:

- quem é (escola, representantes, o que **não** é)
- tese **positiva** (o que defende, não só o que nega — rótulo anti-X não basta)
- **os outros neste tribunal** — uma linha cada, tirada da coluna “Não é” do elenco, para não caricaturar desde o T01
- regras do tribunal (abaixo)
- caminho de `00-protocolo.md` (a tese está lá; nada fora desta pasta)
- a pergunta do turno + eixos da agenda compartilhada
- ordem: gravar `turnos/TNN-<nome>.md` no formato de `templates/turno.md`

Regras que vão na orientação (e no protocolo):

- Citar Escritura no fio (livro, capítulo e versículo junto da declaração; nomear o episódio não basta); distinguir cumprimento, andamento e resto
- Defender a **melhor** versão da própria escola, não a média popular
- Apresente a versão mais forte do outro antes de refutar (na réplica)
- Nomear **perigos da própria posição**, não só os do outro
- Proibido relógio de noticiário, anedota de leigo como refutação da escola, caricatura
- Não ler peças dos outros agentes até o mediador colar a versão mais forte
- Não conceder o que a escola não concede só para parecer irênico
- Idioma do protocolo (padrão: português do Brasil); tom de advogado, não de influenciador
- Teses da seção **Fora do tribunal** do protocolo: ninguém as defende nem as atribui ao outro
- Na réplica, recuse a **versão mais forte do mediador**, não a caricatura. Se a versão mais forte estiver errada, diga em uma linha e recuse o que o outro de fato sustentou

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
9. Nota de turno (N, data, ambiente de execução)

Você lê a síntese (mapa) e o `veredito.md` (e daí). A ata existe para auditar uma frase. Não entregue uma colagem das três conversas. Sem `veredito.md` o ciclo não fechou.

## Verificação de qualidade (obrigatória a cada turno)

Modelo: `templates/qualidade.md` → `qualidade.md` no destino.

O mediador lê as três peças **antes** de atualizar a síntese. Não é opinião: é lista de verificação.

RETRY (regrava o mesmo arquivo, cego, motivo na orientação):

- saiu da escola / defendeu a caricatura de si
- não percorreu a pauta
- atribuiu tese da lista Fora do tribunal
- arquivo ausente ou fora do formato
- editou turno anterior travado
- citação de carga cujo texto não diz o que a peça afirma (versículo errado ou inventado)

WARN (não retrabalha; anota e vira pauta se preciso):

- um eixo em branco
- texto decisivo só um lado citou
- versão mais forte um pouco distorcida, sem caricatura
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

- Lançar agentes (ou criar a pasta) antes da entrevista inicial
- Apontar índice, orientação ou agentes para nota, artigo ou caminho fora da pasta
- Misturar kinds/modelos
- Deixar o segundo agente ver o primeiro no mesmo turno
- Confiar em histórico da tela do Herdr como arquivo
- Colar a transcrição inteira como “resultado”
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
- Compilar livro, livro digital ou `livro/` no encerramento desta skill (aponta `teo-livro`)
- Aludir a um texto ou episódio bíblico sem capítulo e versículo
- Deixar mal-entendido viver até a declaração final
- Declarar vencedor de escola por padrão
- Vocabulário de outro português nas peças quando o idioma for pt-BR (ficheiro, ecrã, de facto)

## Lista de verificação antes de lançar

- [ ] Entrevista inicial via pergunta estruturada (tema, pergunta, tese em prosa, elenco, fora, idioma, destino, autorização)
- [ ] Tese deste debate no protocolo, sem caminho externo
- [ ] `indice.md` auto-contido (tema, pergunta, vozes)
- [ ] Elenco confirmado; os três discordam da pergunta
- [ ] Pasta destino criada com protocolo (agenda + fora do tribunal) + atas + síntese vazia
- [ ] Usuário disse para lançar
- [ ] `HERDR_ENV=1` (ou modo degradado declarado)
- [ ] Mesmo `--kind` nos três
- [ ] Nomes compatíveis com Herdr
- [ ] cwd dos painéis = pasta destino
- [ ] Foco permanece no mediador

## Lista de verificação no fim de cada turno

- [ ] Três arquivos em `turnos/TNN-*` (ou `TF-*`)
- [ ] `qualidade.md` preenchido; RETRY esgotado ou PASS
- [ ] Mal-entendido corrigido neste ciclo, se houve
- [ ] `atas.md` recebeu o turno
- [ ] `sintese.md` atualizada
- [ ] Turnos anteriores intocados (mtime)
- [ ] Próxima pauta sai dos abertos, da mestra ou de um WARN — não de tema novo
- [ ] Se fechou: `raw/veredito.md` e `raw/curadoria.md` existem; `indice.md` aponta o debate, não um volume
- [ ] Toda declaração bíblica de carga nas peças foi conferida (o texto diz o que a frase afirma)
