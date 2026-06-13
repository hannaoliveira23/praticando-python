pessoas = []
dado = []

while True:
    dado.append(str(input('Digite um nome: ')))
    dado.append(float(input('Digite um peso: ')))
    pessoas.append(dado[:])
    dado.clear()

    resp = str(input('Deseja continuar? [S/N] '))[0]
    if resp in 'Nn':
        break

maiorPeso = menorPeso = pessoas[0][1]
for p in pessoas:
    if p[1] > maiorPeso:
        maiorPeso = p[1]
    if p[1] < menorPeso:
        menorPeso = p[1]

print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso cadastrado foi {maiorPeso:.1f}Kg. As pessoas com esse peso são: ', end='')
for p in pessoas:
    if p[1] == maiorPeso:
        print(p[0], end=' ')
print(f'\nO menor peso cadastrado foi {menorPeso:.1f}Kg. As pessoas com esse peso são: ', end='')
for p in pessoas:
    if p[1] == menorPeso:
        print(p[0], end=' ')
print()