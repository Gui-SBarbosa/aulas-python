def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * cria_multiplicador
    return multiplica


# duplica = cria_multiplicador(2)
# duplica = executa(
#     lambda m: lambda n: m * n, 2
# )

# print(duplica())

# print(
#     executa(
#         lambda x, y: x + y, 2, 3
#     ),
#     executa(soma, 2, 3)
# )

print(
    executa(
        lambda *args: sum(args), 1, 2, 3, 4, 5
    )
)
