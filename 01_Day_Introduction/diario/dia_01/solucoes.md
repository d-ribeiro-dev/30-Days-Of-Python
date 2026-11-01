print("Olá!Meu primeiro dia de Python!")

O primeiro dia foi dedicado à introdução ao Python, ao ambiente de desenvolvimento e aos primeiros comandos.

## 1. Preparando o ambiente

Utilizei:
- Python 3.15.2
- Visual Studio Code
- PowerShell

Para verificar a versão instalada no Windows:

```bash
python --version
```

Se esse comando não funcionar, tente:

```bash
py --version
```

O Python Shell é o ambiente interativo, identificado pelo símbolo `>>>`. Nele, podemos digitar comandos e ver os resultados imediatamente.

## 2. Level 1 — Python Shell

**Exercício 1 — Versão do Python**

Verifiquei a versão instalada: Python 3.15.2.

**Exercício 2 — Operações matemáticas**

Utilizei os números 3 e 4:

| Operação | Resultado |
|---|---:|
| `3 + 4` | 7 |
| `3 - 4` | -1 |
| `3 * 4` | 12 |
| `3 % 4` | 3 |
| `3 / 4` | 0.75 |
| `3 ** 4` | 81 |
| `3 // 4` | 0 |

O operador `%` retorna o resto da divisão; `**` representa potência; e `//` realiza divisão inteira, descartando a parte decimal.

**Exercício 3 — Strings**

Pratiquei textos no Python Shell:

```python
"Diná"
"Ribeiro"
"Brasil"
"Estou adorando esse aprendizado."
```

Uma *string* é um texto escrito entre aspas simples ou duplas.

**Exercício 4 — Tipos de dados**

Utilizei a função `type()` para identificar os tipos:

```python
type(10)
type(9.8)
type(3.14)
type(4 - 4j)
type(['Asabeneh', 'Python', 'Finland'])
type("Diná")
type("Ribeiro")
type("Brasil")
```

## 3. Level 2 — Arquivo Python

Criei o arquivo:

`30DaysOfPython/day_1/helloworld.py`

Repeti os exercícios anteriores, agora dentro de um arquivo `.py`.

A principal diferença é que, no arquivo, usei `print()` para exibir os resultados.

Exemplo:

```python
print(3 + 4)
print(type(10))
print("Estou adorando esse aprendizado.")
```

Para executar pelo terminal:

```bash
python helloworld.py
```

## 4. Level 3 — Tipos de dados e distância euclidiana

**Exercício 1 — Exemplos de tipos de dados**

Conheci os principais tipos:

| Tipo | Exemplo |
|---|---|
| Inteiro (`int`) | `10` |
| Decimal (`float`) | `3.14` |
| Complexo (`complex`) | `4 - 4j` |
| Texto (`str`) | `"Python"` |
| Booleano (`bool`) | `True` |
| Lista (`list`) | `[1, 2, 3]` |
| Tupla (`tuple`) | `(1, 2, 3)` |
| Conjunto (`set`) | `{1, 2, 3}` |
| Dicionário (`dict`) | `{"nome": "Diná"}` |

**Exercício 2 — Distância euclidiana**

Calculei a distância entre os pontos `(2, 3)` e `(10, 8)`.

```python
x1, y1 = 2, 3
x2, y2 = 10, 8

distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print(distancia)
```

Resultado:

```text
9.433981132056603
```

O operador `**` representa potência. Quando usamos `** 0.5`, calculamos a raiz quadrada do valor.

## 5. Se algo não funcionar

- **Python não é reconhecido:** tente `py --version`. Se também falhar, verifique a instalação e a configuração do Python no Windows.
- **Arquivo não encontrado:** confira se o terminal está na pasta `day_1` antes de executar o comando.
- **Resultado não aparece:** confira se utilizou `print()` no arquivo.
- **Erro de indentação:** verifique os espaços no início das linhas e mantenha a estrutura do código.

Uma boa prática é ler a mensagem de erro, localizar a linha indicada e verificar o código antes de fazer alterações.

## 6. Conclusão do Dia 1

Neste primeiro dia, pratiquei operações matemáticas, strings, identificação de tipos de dados e execução de arquivos Python.

Também tive meu primeiro contato com a distância euclidiana, relacionando os pontos de um plano cartesiano com um cálculo feito em Python.

**Status:** Dia 1 concluído. 🐍