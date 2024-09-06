"""
enumerate - enumera iteraveis (indices)
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joao')
lista.pop(0)
print(lista)


for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(valor)





 try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
