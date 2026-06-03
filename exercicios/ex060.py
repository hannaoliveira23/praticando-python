a = int(input('Digite um número: '))

cont = a
fat = 1

print('Calculando {}! = '.format(a), end='')
while cont > 0:
    print('{}'.format(cont), end=' ')
    if cont > 1:
        print('x', end=' ')
    else:
        print('=', end=' ')
    fat *= cont
    cont -= 1

print('{}'.format(fat))

# pode ser usado o método factorial da biblioteca math