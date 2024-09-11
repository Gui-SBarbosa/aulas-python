"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
    10  9  8  7  6  5  4  3  2
*   7   4  6  8  2  4  8  9  0
    70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado aterior for maior que 9:
    resultado é 0
contrrio disso:
    resutado é o valor da conta
O primeiro dígito do CPF é 7
"""
#   Que codigo podre
#   Odeio minha vida
cpf_enviado = "746.824.890-70" \
    .replace('.', '') \
    .replace('-', '') \
    .replace(' ', '')
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
