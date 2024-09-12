'''
Iterando strings com while
'''

nome = 'Guilherme'  # Iteráveis
indice = 0

while indice < len(nome):
    indice += 1
    print(f'*{nome[:indice:]}*')

print('Acabou')
