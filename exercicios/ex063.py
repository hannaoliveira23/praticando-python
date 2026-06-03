x = int(input('Digite um número: '))
print('\n{} primeiros termos da sequência de Fibonacci:'.format(x))

cont = 0
e1 = 0
e2 = 1

a = e1
while cont < x:
    print(a, end=' -> ')
    a = e2
    e2 += e1
    e1 = a
    cont += 1
print('FIM')

'''
SOLUÇÃO DO VÍDEO
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
print('~'*30)
'''