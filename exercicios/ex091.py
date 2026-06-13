from random import randint
from time import sleep
from operator import itemgetter

sorteio = dict()
print('VALORES SORTEADOS: ')
for i in range(0,4):
    sorteio[f'Jogador {i+1}'] = randint(1,6)
    print(f'    O Jogador {i+1} tirou {sorteio[f"Jogador {i+1}"]}.')
    sleep(1)

'''
A PARTE ACIMA PODE SER ESCRITA DA SEGUNTE FORMA:
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
'''

print('\nRANKING DOS JOGADORES:')

# sorteio.items() pega tanto a chave quanto o valor.
# key=itemgetter(1) diz para ordenar pelo VALOR (índice 1). Se fosse (0), seria pela CHAVE.
# reverse=True garante que vá do maior para o menor (ordem decrescente).
ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True)

# IMPORTANTE:
# Quando ordenamos um dicionário, o resultado vira uma lista cheia de tuplas, onde cada tupla é um par (Chave, Valor).
# Como exemplo, após a ordenação do dicionário, temos: [('Jogador 2', 6), ('Jogador 4', 5), ('Jogador 1', 3), ('Jogador 3', 2)]

for posição, jogador in enumerate(ranking):
    print(f'    {posição+1}ª posição: {jogador[0]} com {jogador[1]}.')
    sleep(1)