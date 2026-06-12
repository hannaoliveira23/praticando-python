brasileirao = ('Palmeiras', 'Flamengo', 'Fluminense', 'Athletico-PR', 'Red Bull Bragantino', 'Bahia', 'Coritiba', 'São Paulo', 'Atlético-MG', 'Corinthians', 'Cruzeiro', 'Botafogo', 'Vitória', 'Internacional', 'Santos', 'Grêmio', 'Vasco', 'Remo', 'Mirassol', 'Chapecoense')

print(f'Lista de times do Brasileirão (12/06/26): {brasileirao}')
print(f'> 5 primeiros: {brasileirao[:5]}')
print(f'> 4 últimos: {brasileirao[16:]}')
print(f'> Lista em ordem alfabética: {sorted(brasileirao)}')
print(f'> Chapecoense está na {(brasileirao.index('Chapecoense'))+1}ª posição.') 