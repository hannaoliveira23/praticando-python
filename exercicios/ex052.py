from math import sqrt

x = int(input('Digite um número: '))

if x <= 1:
    primo = False
else:
    primo = True

    for i in range(2,int(sqrt(x)+1)):
        if x % i == 0:
            primo = False

if primo:
    print('{}{} É primo.{}'.format('\033[32m', x, '\033[m'))
else:
    print('{}{} NÃO É primo.{}'.format('\033[31m', x, '\033[m'))