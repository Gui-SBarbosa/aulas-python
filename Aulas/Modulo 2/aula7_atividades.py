# Exercicios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# retorne o total para uma varivel e motra o valor
# da variavel


# def mult(*args):
#     resultado = 1
#     for valor in args:
#         resultado *= valor
#     return resultado


# mult_1 = mult(1, 2, 3, 4, 5)
# print(mult_1)

# Crie uma função fala se um numero é par ou impar
# Retorne se o número é par ou impar


def par_impar(numero):
    mult_dois = numero % 2 == 0
    if mult_dois:
        return 'Par'
    return 'Impar'


print(par_impar(5))
