'''
Listas
- mutável
- armazena elementos de diferentes tipos
- lista = []
'''

frutas = ['maçã', 'banana', 'laranja']

print('Acessando os elementos da lista por seus índices:')
print(frutas[0])
print(frutas[1])
print(frutas[2])

print('Acessando os Elm da lista na ordem inversa:')
print(frutas[-1])
print(frutas[-2])
print(frutas[-3])

'''Métodos de listas
A lista é MUTÁVEL
append(elemento) - adiciona um Elm no final da lista
insert(indice, elemento) - insere um Elm em uma posição específica
remove(elemento) - remove a primeira ocorrência do Elm na lista
pop(indice) - remove e retorna um Elm em uma posição específica
sort() - ordena em ordem crescente
reverse() -  inverte a ordem dos Elm
'''

frutas.append('pêra')
print(frutas)

frutas.insert(1, 'uva')
print(frutas)

frutas.remove('banana')
print(frutas)

fruta_removida = frutas.pop(2)
print(fruta_removida)
print(frutas)

frutas.sort()
print(frutas)

frutas.reverse()
print(frutas)

'''
Lista de compreensão - cria lista baseada em uma sequência existente
nova_lista = [expressão for elemento in sequencia if condicão]
'''

numeros = [1, 2, 3, 4, 5]
quadrados = [x**2 for x in numeros if x % 2 == 0]
print(quadrados)

dobro = [2*x for x in numeros]
print(dobro)