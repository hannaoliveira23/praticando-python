lista = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)

    resp = str(input('Deseja continuar? [S/N] '))[0]
    if resp in 'Nn':
        break

print(f'A lista final é: {lista}.')
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'Ordenando em forma decrescente: {lista}')
if 5 in lista:
    print('O valor 5 FOI digitado.')
else:
    print('O valor 5 NÃO FOI digitado.')