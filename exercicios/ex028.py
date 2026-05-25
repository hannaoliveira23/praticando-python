from random import randint
from time import sleep

numComp = randint(0, 5)
numUsu = int(input(('Digite um número de 0 a 5: ')))

print('PROCESSANDO...')
sleep(2)

if numUsu == numComp:
    print('Parabéns! Você acertou o número escolhido pelo computador!')
else:
    print('Infelizmente, não foi dessa vez. O número correto era {}.'.format(numComp))