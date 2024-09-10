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
cpf = input("Digite os noves primeiros digitos do seu cpf: ")

i = 10
lista = []

for numb in cpf:
    numb = int(numb)
    resultado = numb * i
    lista.append(resultado)
    i -= 1

sum_valor = 0

for valor in lista:
    sum_valor += valor

resultado_valor = sum_valor * 10 % 11

if resultado_valor > 9:
    primeiro_valor = 0
else:
    primeiro_valor = resultado_valor

lista2 = [cpf]
lista2.append(str(primeiro_valor))
i = 11

lista3 = []

for numero in lista2:
    for numero in numero:
        numero = int(numero)
        resultado_2 = numero * i
        lista3.append(resultado_2)
        i -= 1

sum_valor_2 = 0

for valor2 in lista3:
    sum_valor_2 += valor2

resultado_valor2 = sum_valor_2 % 11

if resultado_valor2 < 2:
    segundo_valor = 0
else:
    segundo_valor = 11 - resultado_valor2

print(f'{cpf}-{primeiro_valor}{segundo_valor}')
