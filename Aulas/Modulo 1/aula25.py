"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (0123456789ABCDEF)
"""

nome = 'Gui'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadeciaml de %d é %X' % (15, 16))
