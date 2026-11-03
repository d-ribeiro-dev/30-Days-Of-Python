
"""
30 Days of Python — Dia 3: Operators
Registro de estudos e exemplos praticados.
"""

# ==================================================
# 1. BOOLEANOS
# ==================================================

print("1. BOOLEANOS")

print(type(True))       # bool
print(type(False))      # bool
print(type("True"))     # str
print(type(10 > 5))     # bool


# ==================================================
# 2. OPERADORES ARITMÉTICOS
# ==================================================

print("\n2. OPERADORES ARITMÉTICOS")

a = 10
b = 3

print("Adição:", a + b)
print("Subtração:", a - b)
print("Multiplicação:", a * b)
print("Divisão:", a / b)
print("Divisão inteira:", a // b)
print("Resto:", a % b)
print("Potenciação:", a ** b)

# Diferença entre multiplicação e potenciação
print("4 * 2 =", 4 * 2)       # 8
print("4 ** 2 =", 4 ** 2)     # 16


# ==================================================
# 3. OPERADORES DE COMPARAÇÃO
# ==================================================

print("\n3. OPERADORES DE COMPARAÇÃO")

a = 7
b = 12

print(a < b)     # True
print(a > b)     # False
print(a == b)    # False
print(a != b)    # True
print(a <= b)    # True
print(a >= b)    # False


# ==================================================
# 4. OPERADORES LÓGICOS
# ==================================================

print("\n4. OPERADORES LÓGICOS")

idade = 20
tem_carteira = True

print(idade >= 18 and tem_carteira)
print(idade < 18 or tem_carteira)
print(not tem_carteira)


# ==================================================
# 5. OPERADORES DE ATRIBUIÇÃO
# ==================================================

print("\n5. OPERADORES DE ATRIBUIÇÃO")

saldo = 100
saldo += 50
saldo -= 30
saldo *= 2

print("Saldo:", saldo)  # 240

pontos = 20
pontos += 10
pontos *= 3
pontos -= 15

print("Pontos:", pontos)  # 75

# Outros operadores
valor = 20
valor /= 2
print("Divisão:", valor)

valor = 17
valor //= 5
print("Divisão inteira:", valor)

valor = 17
valor %= 5
print("Resto:", valor)

valor = 3
valor **= 2
print("Potenciação:", valor)


# ==================================================
# 6. OPERADORES DE IDENTIDADE
# ==================================================

print("\n6. OPERADORES DE IDENTIDADE")

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

print(lista_a == lista_c)  # True
print(lista_a is lista_c)  # False
print(lista_a is lista_b)  # True

# == compara valores.
# is verifica se é o mesmo objeto.


# ==================================================
# 7. OPERADORES DE ASSOCIAÇÃO
# ==================================================

print("\n7. OPERADORES DE ASSOCIAÇÃO")

frutas = ["uva", "maçã", "banana"]

print("uva" in frutas)          # True
print("pera" in frutas)         # False
print("pera" not in frutas)     # True


# ==================================================
# 8. PRECEDÊNCIA DOS OPERADORES
# ==================================================

print("\n8. PRECEDÊNCIA DOS OPERADORES")

resultado_1 = 10 + 5 * 2
print("Sem parênteses:", resultado_1)  # 20

resultado_2 = (10 + 5) * 2
print("Com parênteses:", resultado_2)  # 30

resultado_3 = 2 + 3 * 4 ** 2
print("Ordem de operações:", resultado_3)  # 50


# ==================================================
# 9. EXERCÍCIOS DE REVISÃO
# ==================================================

print("\n9. EXERCÍCIOS DE REVISÃO")

# Aritmética
numero = 12
resultado = numero // 5 + numero % 5
print("Resultado:", resultado)  # 4

# Comparação
a = 15
b = 20

print(a > b, a < b, a != b)  # False True True

# Lógica
idade = 17
tem_autorizacao = True

print(idade >= 18 and tem_autorizacao)  # False
print(idade >= 18 or tem_autorizacao)   # True
print(not tem_autorizacao)              # False

# Atribuição
valor = 10
valor += 5
valor *= 2
valor -= 8

print("Valor final:", valor)  # 22

# Associação e identidade
frutas = ["uva", "maçã", "banana"]
outra_lista = frutas

print("uva" in frutas)          # True
print("pera" not in frutas)     # True
print(frutas is outra_lista)    # True

# Precedência



print (1)
print(1*1)
print(1*1*1)
print(1*1*1*1)
print(1**1)