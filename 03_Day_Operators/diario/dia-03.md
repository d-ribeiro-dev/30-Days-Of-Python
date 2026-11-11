
# Dia 3 — Operators (Operadores)

**Data:** 03/11/2026
**Curso:** 30 Days of Python — Asabeneh Yetayeh

**Material oficial:** [Day 3 — Operators](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/03_Day_Operators/03_operators.md)

---

## 1. Objetivo

Estudei os operadores do Python, compreendi como utilizá-los em expressões e pratiquei cálculos, comparações, condições lógicas e operações com variáveis.

A aula foi dividida em explicações, exemplos guiados e exercícios. Resolvi as atividades propostas, corrigi respostas quando necessário e refiz cálculos para conferir os resultados.

## 2. Conteúdo estudado

### 2.1. Booleanos

Aprendi que os valores booleanos são:

- `True`: verdadeiro.
- `False`: falso.
- `bool`: tipo de dado booleano.

Também verifiquei a diferença entre `True` e `"True"`: o primeiro é um booleano e o segundo é uma string.

### 2.2. Operadores aritméticos

| Operador | Função |
|---|---|
| `+` | Adição |
| `-` | Subtração |
| `*` | Multiplicação |
| `/` | Divisão |
| `//` | Divisão inteira |
| `%` | Resto da divisão |
| `**` | Potenciação |

Pratiquei operações isoladas e expressões com mais de um operador.

### 2.3. Operadores de comparação

| Operador | Significado |
|---|---|
| `==` | Igual |
| `!=` | Diferente |
| `>` | Maior que |
| `<` | Menor que |
| `>=` | Maior ou igual |
| `<=` | Menor ou igual |

Usei a analogia da boca do crocodilo para lembrar que a abertura do sinal fica voltada para o maior valor.

### 2.4. Operadores lógicos

- `and`: as duas condições precisam ser verdadeiras.
- `or`: pelo menos uma condição precisa ser verdadeira.
- `not`: inverte o resultado lógico.

Pratiquei combinações de condições e conferi os resultados booleanos.

### 2.5. Operadores de atribuição

Estudei e pratiquei:

`=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`

Utilizei variáveis como `saldo`, `pontos` e `valor` para acompanhar como cada operação modifica o valor armazenado.

Exemplo praticado:

```python
saldo = 100
saldo += 50
saldo -= 30
saldo *= 2

print(saldo)  # 240
```

### 2.6. Identidade

Estudei `is` e `is not`.

Compreendi a diferença entre:

- `==`: compara os valores.
- `is`: verifica se duas referências apontam para o mesmo objeto.

Utilizei listas para observar a diferença entre igualdade e identidade.

### 2.7. Associação

Estudei:

- `in`: verifica se um elemento está presente.
- `not in`: verifica se um elemento não está presente.

Pratiquei consultas em listas de frutas e verificações de presença de palavras.

### 2.8. Precedência dos operadores

Pratiquei expressões com parênteses, potenciação, multiplicação, divisão, adição e subtração.

Compreendi que Python segue uma ordem de precedência e que os parênteses podem alterar a ordem dos cálculos.

---

## 3. Exercícios realizados durante a aula

Resolvi atividades de fixação antes e durante a sequência de exercícios.

### 3.1. Booleanos e comparações

- Identifiquei valores verdadeiros e falsos.
- Verifiquei os tipos com `type()`.
- Comparei números utilizando os operadores relacionais.
- Pratiquei condições que retornam `True` ou `False`.

Em uma sequência de comparações, obtive os resultados:

```python
True
False
False
```

### 3.2. Operadores lógicos

Pratiquei combinações de condições usando `and`, `or` e `not`.

Em uma sequência de exercícios, os resultados foram:

```python
True
True
False
```

### 3.3. Operadores de atribuição

Resolvi sequências de operações com variáveis.

Exemplo:

```python
saldo = 100
saldo += 50
saldo -= 30
saldo *= 2
```

Resultado: `240`.

Também resolvi exercícios com outras sequências de atualização de valores.

### 3.4. Identidade e associação

Comparei listas utilizando `is` e `==` e pratiquei a presença ou ausência de elementos com `in` e `not in`.

### 3.5. Cálculos e expressões

Pratiquei:

```python
4 * 2       # 8
4 ** 2      # 16

12 // 5     # 2
12 % 5      # 2

10 + 5 * 2  # 20
(10 + 5) * 2  # 30

2 + 3 * 4 ** 2  # 50
```

Também resolvi expressões maiores, conferindo a ordem de execução das operações.

---

## 4. Exercícios da sequência realizada

Durante a aula, resolvi os exercícios apresentados em sequência, incluindo atividades com tipos numéricos, cálculos geométricos, inclinação, distância, comparação de textos, conversões, paridade, divisão, pagamento e tempo de vida.

Alguns enunciados foram adaptados durante a explicação. Por isso, esta seção registra o trabalho realizado na aula, sem afirmar que todos os enunciados foram reproduzidos exatamente como aparecem no repositório original.

### Registros de respostas e correções importantes

**Tipos numéricos**

- Declarei a idade como inteiro: `44`.
- Declarei a altura como decimal: `1.59`.
- Ao tentar declarar um número complexo, utilizei `44d`. Corrigi após verificar que Python utiliza `j` para a parte imaginária, como em `44j`.

**Inclinação e distância**

- Calculei a inclinação entre os pontos `(2, 2)` e `(6, 10)`.
- Corrigi a identificação das coordenadas e obtive inclinação igual a `2`.
- Calculei a distância utilizando a fórmula da distância euclidiana.
- Corrigi a aplicação das potências: `4² = 16` e `8² = 64`.
- Resultado: `√80 ≈ 8,94`.

**Equação do segundo grau**

Trabalhei com:

```python
y = x**2 + 6*x + 9
```

Verifiquei o valor de `x = -3`:

```python
(-3)**2 + 6*(-3) + 9
```

Resultado: `0`.

**Comprimento e conversões**

Pratiquei o uso de `len()` e conversões de tipos. Também verifiquei o comprimento de uma frase, obtendo `37` caracteres.

**Paridade e divisão**

Reforcei a diferença entre os operadores:

```python
7 % 2   # 1
7 // 2  # 3
7 / 2   # 3.5
```

O operador `%` fornece o resto da divisão e permite verificar se um número é par ou ímpar.

**Tipos de dados**

Revisei a identificação de valores inteiros, decimais, booleanos e complexos.

Também verifiquei que:

```python
int(9.8)  # 9
```

A conversão para inteiro descarta a parte decimal; não arredonda o número.

**Cálculo de pagamento**

Pratiquei o cálculo:

```python
40 * 28
```

Resultado: `1120`.

**Cálculo de segundos vividos**

Pratiquei um cálculo com 30 anos, considerando 365 dias por ano:

```python
30 * 365 * 24 * 60 * 60
```

Resultado: `946080000` segundos.

---

## 5. Conferência com a lista oficial do Asabeneh

A lista oficial contém 23 exercícios. Durante nossa aula, trabalhei os conteúdos e as atividades correspondentes, mas alguns enunciados apresentados foram adaptados ou tiveram sua numeração trocada.

| Exercícios oficiais | Conteúdo | Registro |
|---|---|---|
| 1 a 3 | Idade, altura e número complexo | Praticados |
| 4 a 7 | Área e perímetro de figuras geométricas | Praticados |
| 8 a 11 | Inclinação, distância, comparação de inclinações e equação | Praticados, com diferenças entre alguns enunciados |
| 12 a 16 | Comprimento de palavras, comparações, associação e conversões | Praticados |
| 17 a 20 | Paridade, divisão, tipos e conversão | Praticados, com diferenças em alguns exemplos |
| 21 a 23 | Pagamento, segundos vividos e tabela numérica | Praticados, mas nem todos os enunciados foram reproduzidos exatamente |

**Observação importante:** esta tabela registra as atividades realizadas na aula. Não representa uma validação de que cada código foi executado exatamente conforme o enunciado original. A tabela numérica oficial do exercício 23, por exemplo, é diferente do exemplo de impressão que pratiquei durante a aula.

---

## 6. Dificuldades e aprendizados

Durante os exercícios, identifiquei pontos que precisaram de reforço:

- Diferenciar multiplicação (`*`) de potenciação (`**`).
- Diferenciar divisão inteira (`//`) de resto (`%`).
- Interpretar corretamente os sinais de maior e menor.
- Respeitar a ordem de precedência dos operadores.
- Identificar corretamente as coordenadas nas fórmulas matemáticas.
- Aplicar potências e raízes nos cálculos de distância.
- Diferenciar igualdade (`==`) de identidade (`is`).
- Reconhecer a diferença entre conversão de tipos e arredondamento.

Corrigi respostas, refiz cálculos e conferi os resultados até compreender melhor os conceitos.

## 7. Conclusão

Concluí o estudo dos conteúdos do Dia 3 e realizei as atividades propostas durante a aula.

Percebi que alguns operadores são fáceis de confundir quando aparecem juntos em uma expressão. A prática ajudou a entender melhor como cada um funciona e como Python executa os cálculos.

Também identifiquei que alguns exercícios apresentados durante a aula não correspondiam exatamente aos enunciados originais do repositório. Esse registro evita confundir as atividades que pratiquei com a lista oficial.

## 8. Revisão realizada em 11/11/2026

Retomei o conteúdo do Dia 3 em uma revisão com questões aleatórias, conforme o ciclo de estudos combinado.

**Resultado da revisão:** 13 acertos em 17 questões.

Os erros identificados envolveram:
- Diferença entre divisão inteira (`//`) e resto da divisão (`%`).
- Multiplicação de strings.
- Interpretação do operador lógico `not`.
- Fatiamento (*slicing*).
- Combinação de `and` com operadores de comparação.

A revisão serviu para identificar pontos que precisam de prática adicional. As questões foram de revisão, não uma repetição da lista oficial de exercícios do Dia 3.

## 9. Conclusão e próxima etapa

Em 11/11/2026, retomei os operadores por meio de questões aleatórias e identifiquei os conceitos que ainda exigem reforço.

Na mesma sessão, também dei continuidade aos exercícios oficiais do Dia 4 — Strings, registrados no diário correspondente.

**Próxima etapa:** reforçar os pontos identificados na revisão e continuar a sequência oficial de Strings a partir da questão 15.