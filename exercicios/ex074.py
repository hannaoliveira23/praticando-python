from random import randint

n = ()
for c in range(0,5):
    n += (randint(0, 10),)
# n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print('Os valores gerados foram: ', end='')
for numero in n:
    print(f'{numero} ', end='')

print(f'\nO menor valor é {min(n)}.')
print(f'O maior valor é {max(n)}.')
