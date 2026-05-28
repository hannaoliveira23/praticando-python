from random import choice
from time import sleep

opcoes = ['Pedra', 'Papel', 'Tesoura']

print()
print(f'{'\033[35m'}*-{'\033[m'}'*20)
print(f'{'\033[35m'}Bem vindo(a) à nossa BATALHA DE JOKEMPÔ!{'\033[m'}')
print(f'{'\033[35m'}Vamos ver se você consegue vencer...{'\033[m'}')
print(f'{'\033[35m'}*-{'\033[m'}'*20)

escolhaUsu = str(input(f'\n{'\033[35m'}Digite sua escolha: {'\033[m'}')).strip().lower()
escolhaComp = choice(opcoes).lower()

print(f'\n{'\033[36m'}Vamos lá...{'\033[m'}')
print(f'{'\033[36m'}JO{'\033[m'}')
sleep(0.5)
print(f'{'\033[36m'}KEN{'\033[m'}')
sleep(0.5)
print(f'{'\033[36m'}PÔ!{'\033[m'}')
sleep(0.5)

print('\nEscolha do JOGADOR: {}'.format(escolhaUsu.capitalize()))
print('Escolha do COMPUTADOR: {}'.format(escolhaComp.capitalize()))

if escolhaUsu == escolhaComp:
    print(f'\n{'\033[33m'}EMPATE! Escolhemos a mesma opção .O.{'\033[m'}\n')

elif (escolhaUsu == 'pedra' and escolhaComp == 'tesoura') or (escolhaUsu == 'papel' and escolhaComp == 'pedra') or (escolhaUsu == 'tesoura' and escolhaComp == 'papel'):
    print(f'\n{'\033[32m'}NÃO ACREDITO!!! Você me venceu :({'\033[m'}\n')

else:
    print(f'\n{'\033[31m'}EU VENCI!!! Parece que você não está com sorte hoje ¯\_(ツ)_/¯{'\033[m'}\n')