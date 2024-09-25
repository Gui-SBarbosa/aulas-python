"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao, nome):
    def saudar():
        f'{saudacao}, {nome}'
    return saudar


s1 = criar_saudacao('Bom Dia', 'Guilherme')
s2 = criar_saudacao('Boa Noite', 'Guilherme')
print(s1)
print(s2)
