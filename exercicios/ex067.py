largura = 40
print('-' * largura)
print(f'{"PROGRAMA DA TABUADA":^{largura}}')
print('-' * largura)

while True:
    a = int(input('Você deseja ver a tabuada de qual número? '))
    if a < 0:
        break
    print('-' * largura)
    for i in range(1, 11):
        print(f'{a} x {i} = {a*i}')
    print('-' * largura)
print('FIM DO PROGRAMA DA TABUADA. Volte sempre!')