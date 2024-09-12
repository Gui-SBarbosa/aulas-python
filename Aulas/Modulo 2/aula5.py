"""
Retorno de valores das funções (return)
"""


def soma(x, y):
    if x > 10:
        return 10
    return x + y


soma1 = soma(2, 2)
soma2 = soma(1, 2)
soma3 = soma(3, 2)

print(soma1)
print(soma2)
print(soma3)
print(f'{int(soma1)} + {int(soma2)} =', soma1 + soma2)
