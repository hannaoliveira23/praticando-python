from random import randint
from time import sleep

print('-'*38)
print(f'{'SORTEADOR DE JOGOS MEGA-SENA':^38}')
print('-'*38)

qtdeJogos = int(input('Quantos jogos você deseja gerar?    '))

listaJogos = []
jogo = []
for x in range(0, qtdeJogos):
    for y in range(0, 6):
        num = randint(1,60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    listaJogos.append(jogo[:])
    jogo.clear()

print('PROCESSANDO...')
sleep(1)

for a in range(0, qtdeJogos):
    print(f'Jogo {a+1}: {listaJogos[a]}')
    sleep(0.5)