"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da lista
Não permita que o programa quebre com
erros de indices inexistentes na lista
"""
import os

# Criando variavel da lista
lista = []

# Menu de opções para criar lista
while True:
    print('Bem-Vindo ao seu Menu de Lista de compras')
    print('Seleciona uma Opção: ')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':    # Opção de Inserir um item na lista
        os.system('cls')    # Limpar o terminal
        valor_i = input('Nome do produto: ')
        lista.append(valor_i)
        os.system('cls')
    elif opcao == 'a':  # Retirar um item da lista com base no seu indice
        os.system('cls')
        if len(lista) == 0:
            print('***Nada para apagar!***')
        else:
            for i, name in enumerate(lista):
                print(i, name)
            valor_a = input('Escolha um indice para apagar: ')
            try:
                indice = int(valor_a)
                del lista[indice]
                os.system('cls')
            except ValueError:
                os.system('cls')
                print('Por favor digite número int.')
            except IndexError:
                os.system('cls')
                print('Índice não existe na lista')
            except Exception:
                os.system('cls')
                print('Erro desconhecido')

            # lista.pop(valor_a)
            # os.system('cls')
    elif opcao == 'l':  # Listar todos os itens da lista e seus indices ao lado
        os.system('cls')
        if len(lista) == 0:
            print('***Nada para listar!***')
        else:
            os.system('cls')
            for i, name in enumerate(lista):
                print(i, name)
    elif opcao == 'break':  # Somente para fechar o terminal com comando
        os.system('cls')
        break
    else:
        os.system('cls')
        print('***Opcão inválida!***\n')
