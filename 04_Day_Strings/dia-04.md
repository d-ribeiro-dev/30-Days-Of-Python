# Dia 4 — Strings

**Desafio:** 30 Days of Python — Asabeneh  
**Data de estudo:** 08 e 09/11/2026  
**Tema:** Strings (cadeias de caracteres)

## 1. O que estudei

Neste dia, estudei como trabalhar com strings em Python, desde a criação e manipulação até a consulta e transformação de textos.

Os principais assuntos foram:

- Criação de strings e uso de aspas.
- Comprimento de uma string com `len()`.
- Concatenação de textos.
- Sequências de escape, como `\n`, `\t` e `\\`.
- Formatação de strings com `%`, `.format()` e f-strings.
- Indexação positiva e negativa.
- Fatiamento (*slicing*) e uso de `step`.
- Inversão de strings.
- Desempacotamento (*unpacking*).
- Métodos de strings para localizar, contar, substituir, dividir e organizar textos.

## 2. Prática realizada

Durante o estudo, resolvi exercícios de fixação que utilizamos como prática oficial do nosso percurso no Dia 4.

Entre as atividades realizadas, pratiquei:

- Identificar o tipo de dado com `type()`.
- Contar caracteres com `len()`, incluindo os espaços.
- Concatenar strings.
- Aplicar sequências de escape.
- Formatar textos com diferentes recursos do Python.
- Acessar caracteres por índices.
- Extrair partes de strings com slicing.
- Utilizar intervalos e passos para selecionar caracteres.
- Inverter textos.
- Desempacotar caracteres em variáveis.
- Utilizar métodos como `strip()`, `replace()`, `split()` e `join()`.
- Pesquisar ocorrências com `find()`, `index()` e suas versões reversas.

## 3. Correções e aprendizados importantes

Durante os exercícios, identifiquei alguns pontos que exigiram atenção:

- `len()` conta todos os caracteres, inclusive espaços.
- A concatenação não adiciona espaços automaticamente.
- Os índices começam em zero.
- Índices negativos permitem acessar caracteres a partir do final.
- `find()` e `index()` localizam ocorrências, mas possuem diferenças no comportamento quando o texto procurado não existe.
- `rfind()` e `rindex()` procuram a última ocorrência.
- Em uma mesma string, a posição da segunda ocorrência precisa ser calculada considerando todos os caracteres anteriores.

Também revisamos um erro de cálculo nos índices da string `"IA, Python, IA, Python"`: a primeira ocorrência de `"Python"` começa no índice `4` e a segunda no índice `16`.

## 4. Avaliação do estudo

Consegui praticar diferentes formas de manipular strings e observar como pequenas diferenças na sintaxe e nos índices alteram os resultados.

Alguns conteúdos foram praticados em exercícios com correções e dicas. Por isso, ainda será necessário verificar o que consigo resolver com autonomia.

Os pontos que merecem atenção especial na revisão são as buscas e os índices, principalmente a diferença entre primeira e última ocorrência.

## 5. Retomada dos exercícios oficiais — 11/11/2026

Nesta sessão, dei continuidade à lista oficial de Strings do arquivo `04_strings.md`, mantendo a ordem dos exercícios.

Concluí os exercícios 11 a 14:

- **Exercício 11:** substituição de `Coding` por `Python` com `replace()`.
- **Exercício 12:** substituição de `Everyone` por `All`.
- **Exercício 13:** separação de `Coding For All` usando o espaço como separador com `split(' ')`.
- **Exercício 14:** separação da lista de empresas usando vírgula seguida de um espaço como separador: `split(', ')`.

Reforcei que strings são imutáveis: métodos como `replace()` e `split()` retornam um novo resultado; para manter esse resultado na variável, preciso atribuí-lo novamente.

## 6. Avaliação e pontos para reforçar

Também respondi a uma avaliação de múltipla escolha relacionada aos exercícios seguintes. Como o questionário apresentou problemas na fidelidade de algumas questões e alternativas, não vou considerar a pontuação obtida como uma avaliação definitiva do meu domínio do conteúdo.

Os assuntos que merecem nova verificação prática são:

- Cálculo do último índice de uma string.
- Formação de siglas.
- Identificadores válidos com `isidentifier()`.
- Formatação de strings com cálculos.
- Diferença entre divisão comum (`/`) e divisão inteira (`//`).

Esses pontos ficam registrados como hipóteses de reforço a verificar com exercícios de código, e não como diagnóstico definitivo baseado naquele questionário.

## 7. Próxima etapa

Continuar os exercícios oficiais do Dia 4 a partir da questão 15, preservando os enunciados e a ordem do material original.

Depois, praticar os pontos que exigirem reforço com pequenos códigos, verificando a compreensão na execução e não apenas pelo reconhecimento de alternativas.

**Status:** exercícios oficiais 11 a 14 concluídos nesta sessão; sequência do Dia 4 em andamento.