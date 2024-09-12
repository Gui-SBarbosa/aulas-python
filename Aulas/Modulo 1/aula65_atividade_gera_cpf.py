import random

cpf_9 = ''
for i in range(9):
    cpf_9 += str(random.randint(0, 9))

i = 10

resultado_digito_1 = 0
for numero in cpf_9:
    resultado_digito_1 += int(numero) * i
    i -= 1
primeiro_valor = (resultado_digito_1 * 10) % 11
primeiro_valor = primeiro_valor if primeiro_valor <= 9 else 0

cpf_10 = cpf_9 + str(primeiro_valor)
i2 = 11

resultado_digito_2 = 0
for numero in cpf_10:
    resultado_digito_2 += int(numero) * i
    i2 -= 1
segundo_valor = (resultado_digito_2 * 10) % 11
segundo_valor = segundo_valor if segundo_valor <= 9 else 0

cpf_verificado = f'{cpf_9}{primeiro_valor}{segundo_valor}'

print(cpf_verificado)
