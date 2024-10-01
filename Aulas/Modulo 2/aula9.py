"""
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


s1 = criar_saudacao('Bom Dia')
s2 = criar_saudacao('Boa Tarde')
s3 = criar_saudacao('Boa Noite')

print(s1('Guilherme'))
print(s2('Guilherme'))
print(s3('Guilherme'))
