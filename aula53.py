"""
for in com listas
Maria
Helena
Luiz
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Guilherme')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
