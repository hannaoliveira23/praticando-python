jogadores = list()
jogador = dict()
while True:
    jogador['nome'] = str(input('\nNome do jogador: '))
    jogador['qtdePartidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    cont = total = 0
    gols = list()
    while cont < jogador['qtdePartidas']:
        qtdeGols = int(input(f'Quantos gols na partida {cont+1}? '))
        gols.append(qtdeGols)
        total += qtdeGols
        cont += 1
    jogador['gols'] = gols[:]
    jogador['total'] = total

    jogadores.append(jogador.copy())
    jogador.clear()

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print()
print('-'*40)
print(f'{'APROVEITAMENTO GERAL':^40}')
print('-'*40)
print(f'{'CÓDIGO':<8}{'NOME':<10}{'GOLS':<15}{'TOTAL':>7}')

for pos, player in enumerate(jogadores):
    print(f'{pos:<8}{player["nome"]:<10}{str(player["gols"]):<15}{player["total"]:>7}')
print('-'*40)

while True:
    resp = int(input('Mostrar dados de qual jogador? (999 para interromper) '))
    if resp == 999:
        break

    if resp >= len(jogadores) or resp < 0:
        print(f'Erro! Não existe jogador com o código {resp}. Tente novamente.')
        print()
        continue

    print(f'\nLEVANTAMENTO DO JOGADOR {jogadores[resp]["nome"].upper()}:')
    print(f'O jogador {jogadores[resp]["nome"]} jogou {jogadores[resp]["qtdePartidas"]} partidas.')
    cont = 0
    while cont < jogadores[resp]['qtdePartidas']:
        print(f'    => Na partida {cont+1}, fez {jogadores[resp]["gols"][cont]} gols.')
        cont += 1
    print(f'No total, fez {jogadores[resp]["total"]} gols.')
    print()
print('Volte sempre :)')