int1 = input('Digite um valor: ')
int2 = input('Digite um valor: ')

primeiro_valor = int(int1)
segundo_valor = int(int2)

confirmacao_1 = primeiro_valor > segundo_valor
confirmacao_2 = segundo_valor > primeiro_valor
confirmacao_3 = primeiro_valor == segundo_valor

if confirmacao_1:
    print(f'O {primeiro_valor=} é maior que o {segundo_valor=}')
elif confirmacao_2:
    print(f'O {segundo_valor=} é maior que o {primeiro_valor=}')
elif confirmacao_3:
    print(f'O {primeiro_valor=} é igual o {segundo_valor=}')
else:
    print('Insira valores!')
