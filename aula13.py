nome = 'Guilherme Sousa'
altura = 1.8
peso = 75
imc = peso / (altura ** 2)

# f-strings

linha_1 = f'{nome} tem {altura}m de altura'
linha_2 = f'pesa {peso}Kg, e seu IMC é: {imc:.2f}'

print(linha_1)
print(linha_2)
