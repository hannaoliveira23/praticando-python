# valores = [int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: '))]
valores = []
for n in range(0,5):
    valores.append(int(input('Digite um valor: ')))

maior = menor = valores[0]
for a in valores:
    if a > maior:
        maior = a
    if a < menor:
        menor = a

print(f'A lista digitada foi: {valores}')
print(f'O maior valor é {maior}. Ele foi digitado na(s) posição(ões): ', end='')
for pos, n in enumerate(valores):
    if maior == n:
        print(pos, end='-')
print(f'\nO menor valor é {menor}. Ele foi digitado na(s) posição(ões): ', end='')
for pos, n in enumerate(valores):
    if menor == n:
        print(pos, end='-')
print()
# o maior/menor poderia ser encontrado usando o sort/sorted