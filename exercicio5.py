cont = 1
a = 0
while cont <= 15:
    num = int(input('Insira um número: '))
    if num % 3 == 0:
        a += 1
    cont += 1
print(f'O somatório dos números ímpares é de: {a}')