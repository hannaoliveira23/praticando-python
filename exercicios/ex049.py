num = int(input('Digite um número: '))

print('\nTabuada do {}:'.format(num))
for i in range(0,11):
    print('{} x {} = {}'.format(num, i, num*i))
