from time import sleep

def maior(*valores):
    # valores é uma tupla!
    print('-'*40)
    print('Valores analisados: ')
    maior = valores[0]
    for i in range(0, len(valores)):
        print(valores[i], end=' ')
        if maior < valores[i]:
            maior = valores[i]
    print(f'\nForam analisados {len(valores)} valores ao todo.')
    if len(valores) == 0:
        print('Não há um maior, já que não foi informado nenhum valor.')
    else:
        print(f'O maior valor informado foi {maior}.')


maior(1, 4, 9, 7, 3)
sleep(2)
maior(785, 236, 964)
sleep(2)
maior(1205, 1206)
sleep(2)