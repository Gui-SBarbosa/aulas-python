"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1


def escopo():
    # global x
    x = 10

    def outra_funcao():
        # global x
        x = 11
        y = 2
        print(f'valor dentro da funcao dentro da funcao {x}, {y}')

    outra_funcao()
    print(f'valor dentro da funcao {x}')


print(f'valor fora antes da funcao {x}')
escopo()
print(f'valor fora depois da funcao {x}')
