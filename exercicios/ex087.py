matriz = [[], [], []]
cont = 0
for i in range(0,3):
    for j in range(0,3):
        matriz[i].append(int(input(f'Digite um número para a posição [{i},{j}]: ')))

print('\nMATRIZ FINAL:')
for a in range(0,3):
    for b in range(0,3):
        print(f'[ {matriz[a][b]} ]', end='')
    print()

# SOMA DOS NÚMEROS PARES
somaPares = 0
for x in range(0,3):
    for y in range(0,3):
        if matriz[x][y] % 2 == 0:
            somaPares += matriz[x][y]
print(f'\nA soma dos números pares é {somaPares}.')

# SOMA DA TERCEIRA COLUNA
soma3aColuna = 0
for m in range(0,3):
    soma3aColuna += matriz[m][2]
print(f'A soma dos valores na terceira coluna é {soma3aColuna}.')

# MAIOR VALOR DA SEGUNDA LINHA
maiorValor2aLinha = matriz[1][0]
for n in range(1,3):
    if matriz[1][n] > maiorValor2aLinha:
        maiorValor2aLinha = matriz[1][n]
print(f'O maior valor da segunda linha é {maiorValor2aLinha}.')