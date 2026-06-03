from random import randint

print('{}Vamos ver se você consegue acertar o número que pensei...{}'.format('\033[33m','\033[m'))

numComp = randint(0,10)
numUsu = int(input('Digite um número: '))

conTentativas = 1
while numUsu != numComp:
    numUsu = int(input('Você errou! Tente novamente: '))
    conTentativas += 1
print('Você acertou com {} tentativas.'.format(conTentativas))

'''
SOLUÇÃO DO VÍDEO

from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
'''