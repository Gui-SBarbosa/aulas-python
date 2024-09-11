# Calculadora com while

# Escolher os Dois número e o operador
while True:
    numb_1 = input('Digite um número: ')
    numb_2 = input('Digite outro número: ')
    operador = input('Digite um operador (+-/*): ')

# Criando variáveis
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

# Convertendo variáveis para FLOAT
    try:
        num_1_float = float(numb_1)
        num_2_float = float(numb_2)
        numeros_validos = True
    except Exception:
        numeros_validos = None

# Verificando se o(s) número(s) for(em) invalido(s)
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos')
        continue

    operador_permitidos = '+-/*'

# Verificando se tem um operador válido
    if operador not in operador_permitidos:
        print('Operador inválido!')
        continue

# Verificando se não foi colocado mais de um operador
    if len(operador) > 1:
        continue

    print('Realizando sua conta. Confira o resultado abaixo')

# Calculos sendo realizados de acordo com os números e operador
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = ', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = ', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} = ', num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} = ', num_1_float * num_2_float)
    else:
        print('Nunca deveria chegar aqui')

# Sair
    sair = input('Qur sair? [s]im ').lower().startswith('s')

    if sair is True:
        break
