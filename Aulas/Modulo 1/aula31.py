"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
condicao = True
passou = None

if condicao:
    passou = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou is None:
    print('Não passou')

if passou is not None:
    print('Passou no if')
