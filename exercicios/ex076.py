listagem = ('Impressora', 749.90, 'Caixa de Som', 1169, 'Garrafa Térmica', 29.44, 'Tênis', 195.90)

print('-'*50)
print(f'{'LISTAGEM DE PREÇOS':^50}')
print('-'*50)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<40}', end='')
    else:
        print(f'R${listagem[pos]:>8.2f}')
    