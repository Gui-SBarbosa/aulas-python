# Exercício - sistema de perguntas e respostas
# import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
pontos = 0

#   Minha solução

# usuario = input('Qual seu nome? ')
# os.system('cls')

# pergunta_1 = perguntas[0]['Opções']
# print(perguntas[0]['Pergunta'])

# for i, opcao in enumerate(pergunta_1):
#     print(f'{i}){opcao}')

# resposta = input('Escolha sua resposta: ')

# if resposta == '2':
#     print('Parabéns acertou!\n')
#     pontos += 1
# else:
#     print('Resposta errada!\n')

# pergunta_2 = perguntas[1]['Opções']
# print(perguntas[1]['Pergunta'])

# for i, opcao in enumerate(pergunta_2):
#     print(f'{i}){opcao}')

# resposta = input('Escolha sua resposta: ')

# if resposta == '0':
#     print('Parabéns acertou!\n')
#     pontos += 1
# else:
#     print('Resposta errada!\n')

# pergunta_3 = perguntas[2]['Opções']
# print(perguntas[2]['Pergunta'])

# for i, opcao in enumerate(pergunta_3):
#     print(f'{i}){opcao}')

# resposta = input('Escolha sua resposta: ')

# if resposta == '1':
#     print('Parabéns acertou!')
#     pontos += 1
# else:
#     print('Resposta errada!')

# os.system('cls')
# print(f'Questionario Finalizado!\n{usuario} acertou {pontos} questão(ões)!')


#   Resolução Aula

# for pergunta in perguntas:
#     print('Pergunta:', pergunta['Pergunta'])
#     print()

#     opcoes = pergunta['Opções']
#     for i, opcao in enumerate(opcoes):
#         print(f'{i})', opcao)
#         print()

#     escolha = input('Escolha uma opção: ')
#     acertou = False
#     escolha_int = None
#     qtd_opcoes = len(opcoes)

#     escolha_int = None
#     if escolha.isdigit():
#         escolha_int = int(escolha)

#     if escolha_int is not None:
#         if escolha_int >= 0 and escolha_int < qtd_opcoes:
#             if opcoes[escolha_int] == pergunta['Resposta']:
#                 acertou = True
#     print()
#     if acertou:
#         print('Acertou!')
#         pontos += 1
#     else:
#         print('Errou!')

# print(f'Você acertou {pontos}/3!')
