"""
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador
"""

# texto = iter('Guilherme')  # .__iter__()

# print(next(texto))  # .__next__()

texto = 'Guilherme'  # iteravel
iteratador = iter(texto)  # iterador/iterator

while True:
    try:
        print(next(iteratador))
    except StopIteration:
        break
