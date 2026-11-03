🐍 Dia 2 — Variáveis, tipos de dados e conversões

🎯 Objetivo

Compreender como armazenar informações em variáveis, identificar os tipos de dados utilizados no Python e realizar conversões quando necessário.

📚 1. Funções integradas

Conheci algumas funções nativas do Python:

Função

Para que serve

print()

Exibe informações na tela

input()

Recebe informações digitadas pelo usuário

type()

Identifica o tipo de dado

len()

Retorna a quantidade de elementos

sum()

Soma valores numéricos

📦 2. Variáveis

Variáveis armazenam valores que podem ser utilizados durante a execução do programa.

nome = "Ana"
idade = 25
altura = 1.65

Regras e boas práticas:

Utilizar nomes que indiquem o conteúdo armazenado.

Preferir snake_case para nomes compostos.

Python diferencia letras maiúsculas e minúsculas.

O sinal = representa atribuição de valor.

Também vi que é possível atribuir valores a várias variáveis em uma única instrução.

🔠 3. Tipos de dados

Conheci os principais tipos:

Tipo

Exemplo

str

"Python"

int

25

float

1.65

complex

2 + 3j

bool

True ou False

list

[1, 2, 3]

tuple

(1, 2, 3)

set

{1, 2, 3}

dict

{"nome": "Ana"}

🔄 4. Conversão de tipos (Type Casting)

Aprendi que podemos converter valores usando funções como:

str() — converte para texto.

int() — converte para inteiro.

float() — converte para número decimal.

bool() — converte para verdadeiro ou falso.

list(), tuple() e set() — convertem para coleções correspondentes.

Atenção: nem toda conversão é possível diretamente.

int("50")    # Funciona
int("50.5")  # Gera ValueError

Para converter o texto "50.5" em inteiro, podemos primeiro convertê-lo para float:

int(float("50.5"))  # Resultado: 50

🧺 5. Coleções

Coleção

Características

list

Ordenada, mutável e permite duplicados

tuple

Ordenada e imutável

set

Não permite elementos duplicados

dict

Armazena informações em pares de chave e valor

Exemplos:

frutas = ["maçã", "banana", "uva"]
frutas.append("laranja")

coordenadas = (10, 20)

numeros = {1, 2, 2, 3}

produto = {
    "nome": "Notebook",
    "preco": 2200
}

produto["preco"] = 2300

🧪 6. Experimento prático no VS Code

Testei a entrada de informações pelo usuário e identifiquei os tipos de dados recebidos.

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)

print(type(nome))
print(type(idade))
print(type(altura))

O que observei:

input() retorna texto (str).

int() transforma a idade em inteiro.

float() transforma a altura em decimal.

type() permite conferir o tipo armazenado.

🛠️ 7. Registro de erros e descobertas

Nesta sessão, fiz exercícios de memória e prática sem consultar exemplos. Alguns erros apareceram durante a execução.

Erro 1 — Instruções na mesma linha

Tentei escrever várias instruções sem separá-las corretamente.

nome = "Ana" idade = "25" print(idade)

O Python retornou SyntaxError.

Descoberta: cada instrução precisa estar corretamente separada. Neste exercício, organizamos cada comando em uma linha.

Erro 2 — Parêntese não fechado

Ao testar:

print(str(idade)

O comando ficou incompleto. O interpretador indicou que ainda esperava a continuação da instrução.

Correção: fechar o parêntese que faltava.

Erro 3 — Confusão entre type() e str()

Durante o exercício, confundi duas funções com objetivos diferentes:

type() verifica o tipo de um valor.

str() converte um valor para texto.

Uma função não substitui a outra.

💡 8. Uma descoberta importante: converter não é o mesmo que reatribuir

Testamos duas situações:

Conversão apenas durante a exibição:

idade = 25

print(str(idade))
print(type(idade))

A conversão acontece dentro do print(), mas a variável continua armazenando um inteiro.

Conversão e armazenamento na variável:

idade = 25

idade = str(idade)

print(type(idade))

Agora o valor convertido foi atribuído novamente à variável. Portanto, seu tipo passou a ser str.

🧠 9. O que preciso reforçar

Recuperar de memória as funções type() e str().

Diferenciar identificação de tipo e conversão.

Entender quando uma conversão altera apenas a exibição e quando altera o valor armazenado.

Praticar a escrita de instruções sem consultar exemplos.

Continuar desenvolvendo a leitura de mensagens de erro.

✅ Conclusão do Dia 2

O objetivo desta sessão foi conhecer e experimentar conceitos fundamentais do Python.

Nem todas as instruções foram lembradas de primeira. Com tentativas, observação dos resultados e pistas, conseguimos identificar erros e chegar às correções.

Aprendizado importante: não basta fazer o código funcionar. Precisamos entender por que funcionou e o que mudou durante a execução.git dd