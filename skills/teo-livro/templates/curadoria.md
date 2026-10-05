# Curadoria

Não escolhe escola. Confere se o **volume** é um livro: fio, cadeia, fontes, compilação.

Quem redigiu o capítulo não é o único olho. Prefira subagente isolado.

**Veredito:** PASS / PASS com WARN / RETRY

## 1. Processo

- [ ] `raw/pesquisa.md` lista fontes *lidas* (turnos, se debate)
- [ ] Orientação com fio ≤20 palavras e destino
- [ ] Plano de capítulos com emprego + destino por capítulo
- [ ] Esboço reverso do volume
- [ ] Editor de desenvolvimento isolado (ou passe posterior contra o arquivo)
- [ ] Checagem de fontes de carga

Falta de ficha em `raw/` → o processo não aconteceu. Não é WARN cosmética: complete ou RETRY.

## 2. Cadeia

- [ ] As primeiras frases dos parágrafos, em sequência, sobem um degrau
- [ ] Cada capítulo senta
- [ ] O volume senta no destino da orientação
- [ ] Sem *e então* entre seções que deveriam ser consequência ou contraste

Falha de cadeia → RETRY do capítulo, não «passa com estilo».

## 3. Referências

| Ref. | Capítulo | A frase afirma | O texto diz isso? | Nota |
|---|---|---|---|---|
| | | | sim / leitura da escola / não | |

`não` numa citação de carga → RETRY do capítulo.

Alusão sem livro-capítulo-versículo → WARN, e complete.

## 4. Produção

- [ ] `asciidoctor livro/_index.adoc` compila
- [ ] `_index.adoc` inclui todos, na ordem do plano de capítulos
- [ ] `[[id]]` únicos; referências cruzadas resolvem
- [ ] Idioma da orientação; sem vocabulário de outro português se for pt-BR
- [ ] Sem T01, apresentação da versão mais forte do argumento, mesa, instrução de montagem, `[dedication]`
- [ ] Glossário + notas na primeira ocorrência dos termos inevitáveis
- [ ] Se o insumo foi debate: nenhuma tese que o turno não sustentou

## Falhas deste passe

| Tipo | Onde | O que fazer |
|---|---|---|
| | | RETRY capítulo / completar fonte / WARN |

## Veredito

PASS | PASS com WARN | RETRY
