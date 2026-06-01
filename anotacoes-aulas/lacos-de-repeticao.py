# 1. Laço com variável de controle
#    for c in range(1,10): - NÃO CONSIDERA O ÚLTIMO NÚMERO (1,2,3,4,5,6,7,8,9)
#    for c in range (0,7,2): - TERCEIRO NÚMERO: O QUE ACONTECE (nesse caso, pula de 2 em 2)

for c in range(0,6):
    print('Oi')
print('FIM')

for c in range(0,6):
    print(c)
print('FIM')

for c in range(6,0,-1):
    print(c)
print('FIM')

for c in range(0,7,2):
    print(c)
print('FIM')

n = int(input('Digite um número: '))
for c in range(0,n+1):
    print(c)
print('FIM')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i,f+1,p):
    print(c)
print('FIM')