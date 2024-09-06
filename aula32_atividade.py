"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# num = input('Digite um número: ')

# if num.isdigit():  # Confirmar se tem apenas número na String
#     num_int = int(num)
#     par_impar = num_int % 2 == 0    # Verificar se o número é par ou impar
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {num_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# entrada = input('Quantas horas é agora? ')

# try:
#     horas = int(entrada)

#     if horas <= 11:
#         print('Bom Dia!')

#     elif horas >= 12 and horas <= 17:
#         print('Boa Tarde!')

#     elif horas >= 18 and horas <= 23:
#         print('Boa Noite!')

#     else:
#         print('Não conheço essa hora')
# except NameError:
#     print('Nenhum número foi colocado!')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras
ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

# nome = input('Coloque seu nome: ')

# if len(nome) <= 4:
#     print(f'Seu nome é curto e tem {len(nome)} letras')
# elif len(nome) >= 5 and len(nome) <= 6:
#     print(f'Seu nome é normal e tem {len(nome)} letras')
# elif len(nome) > 6:
#     print(f'Seu nome é muito grande e tem {len(nome)} letras')
