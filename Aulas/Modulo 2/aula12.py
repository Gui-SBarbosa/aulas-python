#   Manipulando chaves e valores em dicionarios
pessoa = {
    # 'nome': 'Guilherme',
    # 'sobrenome': 'Barbosa',
    # 'idade': 18,
    # 'altura': 1.8,
    # 'endereços0': [
    #     {'rua': 'tal tal', 'numero': 123},
    #     {'rua': 'outra rua', 'número': 321}
    # ],
}

chave = 'nome'

pessoa[chave] = 'Cecilia'
pessoa['sobrenome'] = 'Silva'

del pessoa['sobrenome']

print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
    print('bruh')
else:
    print('1')
