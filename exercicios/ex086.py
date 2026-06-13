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