"""
Repetições
while(enquanto)
executa uma ação enquanto a condição for verdadeira
Loop infinito -> Quando o código nao tem fim
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        continue

    print(contador)

    if contador == 40:
        break
print('Acabou')
