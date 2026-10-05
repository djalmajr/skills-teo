# Entrevista inicial

Rode **antes** de criar a pasta e **antes** de lançar agentes. O debate nasce destas respostas, não de um arquivo que já existia.

Use a ferramenta de pergunta estruturada do ambiente de execução (`ask_user_question` no Grok; `AskUserQuestion` no Claude Code; `question` no OpenCode). Um cartão, várias perguntas. Segunda rodada só se a resposta for fina.

Não abra nota, artigo ou caminho de coleção de notas como fonte. Se o usuário apontar um arquivo, peça a tese em prosa neste cartão. Agentes deste debate só leem o que está **dentro** da pasta destino.

## Cartão 1

1. **Qual é o tema deste debate?**
   - Uma frase. Não um caminho. Opções = o que o usuário já disse + domínios comuns (escatologia, soteriologia, dons, batismo). `Other` = o tema em uma frase.

2. **Qual é a pergunta real?**
   - A disputa em uma frase, a que os três devem discordar. Se o tema for escatologia, a opção recomendada pode ser a pergunta do catálogo `escatologia-milenio`. `Other` = a pergunta nas palavras dele.

3. **O que este debate testa?** (seleção múltipla)
   - Premissas que o usuário quer ver sobreviver a três leituras.
   - Se uma premissa é chão compartilhado ou a briga.
   - Três escolas no mesmo feixe de Escritura.
   - `Other` = 3–6 frases da tese *deste* debate (não “veja a nota X”).

4. **Quais três escolas sentam à mesa?**
   - Catálogo `escatologia-milenio` (recomendado se o tema for escatologia).
   - Propor três a partir do tema, depois confirmar.
   - `Other` = nomear as três, com representantes.

5. **O que ninguém deve defender nem atribuir ao outro?**
   - Caricaturas padrão do elenco (recomendado).
   - `Other` = listar.

6. **Em que idioma saem as peças?**
   - Português do Brasil (recomendado; padrão).
   - Português de Portugal.
   - `Other` = outro idioma.

7. **Onde vive o dossiê?**
   - `Debate - <tema>/` no diretório atual (recomendado).
   - `Other` = nome da pasta.

8. **Próximo passo?**
   - Só montar o protocolo; eu confirmo o elenco.
   - Montar e lançar os três agentes.
   - Ainda não: a pergunta precisa de outra rodada.

Leia `elencos.md` **depois** das respostas, para nomear ids e a coluna “Não é”. Não misture clássico com progressivo, nem histórico com relógio de noticiário. Se duas escolas dão a mesma resposta à pergunta real, funda-as num assento.

## Cartão 2 (só se precisar)

Rode de novo se:

- o “tema” foi um caminho ou um “leia a nota”
- faltou a pergunta real
- a tese veio como referência a outro arquivo
- dois assentos concordariam na pergunta

Perguntas típicas da segunda rodada: a tese em 3–6 frases; a pergunta em uma frase; as três escolas com o que cada uma *não* é.

## O que a entrevista inicial grava

Preencha `00-protocolo.md` (seção **Tese deste debate**, **Idioma**) e `indice.md` com prosa própria: tema, pergunta, tese, vozes. Sem “tese em exame”, sem caminho fora da pasta.

Não lance agentes enquanto a pergunta 8 não autorizar o lançamento.

O idioma do protocolo governa turnos, síntese e veredito. Padrão: português do Brasil. Sem vocabulário de outro português (ficheiro, ecrã, de facto) a menos que a entrevista inicial tenha pedido isso.

Livro não nasce nesta entrevista inicial. Se o usuário quiser volume depois, a skill `teo-livro` tem entrevista inicial própria.
