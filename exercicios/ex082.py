lista = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)

    resp = str(input('Deseja continuar? [S/N] '))[0]
    if resp in 'Nn':
        break

listaPares = []
listaImpares = []
for n in lista:
    if n % 2 == 0:
        listaPares.append(n)
    else:
        listaImpares.append(n)

print(f'Lista original: {lista}')
print(f'Lista pares: {listaPares}')
print(f'Lista ímpares: {listaImpares}')