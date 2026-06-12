t = ()
for c in range(0, 4):
    v = int(input('Digite um valor: '))
    t += (v,)
# t = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')), int(input('Digite mais um valor: ')), int(input('Digite o último valor: ')))

print(f'\nVocê digitou os valores {t}.')

print(f'O 9 apareceu {t.count(9)} vezes.')
if 3 in t:
    print(f'O 3 aparece na {t.index(3)}ª posição.')
else:
    print('O 3 não foi digitado.')

contPares = 0
for pos, num in enumerate(t):
    if num % 2 == 0:
        if contPares == 0:
            print('Os valores pares digitados foram: ', end='')
        print(f'{num} ', end='')
        contPares += 1
print()