x = 0
quant = 0
for c in range(0, 6):
    valor = int(input())
    if(valor % 2 == 0):
        x += valor
        quant += 1

print('O total de pares são: {}\nE a soma é: {}'.format(quant, x))
