x = int(input('Digite um número: '))

maior = x
menor = x
cont = 1
soma = x

resp = str(input('Você deseja continuar [S/N]? ')).upper()
while resp != 'N':
    x = int(input('Digite um número: '))
    if x > maior:
        maior = x
    if x < menor:
        menor = x
    cont += 1
    soma += x

    resp = str(input('Você deseja continuar [S/N]? ')).upper()
print('Você digitou {} valores.'.format(cont))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
print('A média dos valores digitados é igual a {:.2f}.'.format(float(soma/cont)))
