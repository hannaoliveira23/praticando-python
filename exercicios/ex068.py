from random import randint

cont = 0
print('Vamos jogar par ou ímpar!')
while True:
    usuario = int(input('\nDigite um valor: '))
    computador = randint(0,10)

    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    soma = usuario + computador

    print(f'\nO computador escolheu {computador}. A soma é igual a {soma}, ', end='')
    if soma % 2 == 0:
        print('que é um número par.')
    else:
        print('que é um número ímpar.')

    venceu = (soma % 2 == 0 and escolha == 'P') or (soma % 2 != 0 and escolha == 'I')
    if not venceu:
        break
    
    print('Parabéns, você venceu! Vamos novamente...')
    cont += 1
print(f'\nGAME OVER! Você venceu {cont} vezes consecutivas.')