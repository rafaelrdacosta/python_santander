#Incluir caracteres especiais utilizando o escape \
print('\"Olá Mundo!\"')

#Operadores aritméticos
a = 10
b = 3

soma = a + b 
print(f'Soma = {soma}')

subtracao = a - b
print(f'Subtração = {subtracao}')

multiplicao = a * b
print(f'Multiplicação = {multiplicao}')

divisao = a / b
print(f'Divisão = {divisao}')

divisao_inteira = a // b
print(f'Divisão inteira = {divisao_inteira}')

modulo = a % b
print(f'Resto da divisão = {modulo}')

exponenciacao = a ** b
print(f'Exponenciação = {exponenciacao}')

#Operadores de comparação
igual = a == b
print(f'Igual? {igual}')

diferente = a != b
print(f'Diferente? {diferente}')

maior = a > b
print(f'Maior que? {maior}')

menor = a < b
print(f'Menor que? {menor}')

maior_igual =  a >= b
print(f'Maior ou igual? {maior_igual}')

menor_igual = a <= b
print(f'Menor igual? {menor_igual}')

#Operadores lógicos
resultado_and = (a > 5) and (b < 5)
print(resultado_and)

resultado_or = (a > 15) or (b < 5)
print(resultado_or)

resultado_not = not (a > 5)
print(resultado_not)