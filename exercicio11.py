n = int(input('Informe o valor de N: '))

cont = 1
s = 0
while cont <= n:
    s += 1/cont
    cont += 1
print(f'A soma é {s}')