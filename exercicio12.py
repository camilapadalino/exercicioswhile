numero = int(input('Informe um número: '))

fatorial = 1
while numero >= 1:
    fatorial *= numero
    numero -= 1
print(f'Fatorial: {fatorial}')