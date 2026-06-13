valores = []
while True:
    num = int(input('Digite um número: '))
    if num in valores:
        print('Valor duplicado! Não será adicionado na lista.')
    else:
        valores.append(num)
        print('Valor adicionado com sucesso!')
    
    resp = str(input('Deseja continuar? [S/N] '))[0]
    if resp in 'Nn':
        break

valores.sort()
print(f'Os valores digitados foram {valores}.')