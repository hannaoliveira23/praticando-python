maior = 0
menor = 0

for i in range(0,5):
    peso = float(input('Digite o peso (em Kg): '))

    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso

        if peso < menor:
            menor = peso

print('O maior peso lido foi {}Kg e o menor foi {}Kg.'.format(maior, menor))