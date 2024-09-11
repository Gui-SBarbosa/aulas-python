import re
import sys

#   Que codigo podre
#   Odeio minha vida
entrada = input('CPF: ')
cpf_enviado = re.sub(
    r'[^0-9]',
    '',
    "746.824.890-70"
    )

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print("Você mandou dados sequenciais!")
    sys.exit()

cpf_9 = cpf_enviado[:9]
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

if cpf_verificado == cpf_enviado:
    print(f"{cpf_enviado} é Válido!")
else:
    print("CPF é Inválido!")
