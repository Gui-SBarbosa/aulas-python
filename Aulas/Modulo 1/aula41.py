frase = 'O Python é uma linguagem de programação'\
    'multiparadigma'\
    'Python foi criado por Guido Van Rossum.'

i = 0
qtd_apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''

# Comando vai continuar sendo executado enquanto I for menor que a Frase
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

# Contar quantas vezes a letra apareceu
    qtd_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_que_apareceu_mais_vezes = letra_atual

    i += 1
print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_que_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)
