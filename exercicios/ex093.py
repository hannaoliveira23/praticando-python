jogador = dict()
jogador['nome'] = str(input('Nome do jogador: '))
jogador['qtdePartidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

cont = total = 0
gols = list()
while cont < jogador['qtdePartidas']:
    qtdeGols = int(input(f'Quantos gols na partida {cont+1}? '))
    gols.append(qtdeGols)
    total += qtdeGols
    cont += 1
jogador['gols'] = gols[:]
jogador['total'] = total # ou sum(gols)

print(f'\nDICIONÁRIO: {jogador}')

for c, v in jogador.items():
    print(f'    > O campo "{c}" tem o valor {v}.')

print('\nINSIGHT GERAL:')
print(f'O jogador {jogador["nome"]} jogou {jogador["qtdePartidas"]} partidas.')
cont = 0
while cont < jogador['qtdePartidas']:
    print(f'    => Na partida {cont+1}, fez {jogador["gols"][cont]} gols.')
    cont += 1
print(f'No total, fez {total} gols.')