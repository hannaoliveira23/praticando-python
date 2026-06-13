from time import sleep

def contador(i, f, p):
    print('-'*40)

    p = 1 if p == 0 else abs(p)

    print(f'Contagem de {i} até {f} de {p} em {p}:')

    passo = p if i < f else -p
    fim = f + 1 if i < f else f - 1

    for x in range(i, fim, passo):
        print(f'{x}', end=' ', flush=True)
        sleep(0.5)
    
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)

print('-'*40)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
contador(inicio, fim, passo)