from time import sleep
n1 = int(input('\nPrimeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0
while opcao != 5:
    opcao = int(input('\nO que você deseja fazer?\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Digitar novos números\n[5] Sair do programa\n> '))
    if opcao == 1:
        print('A soma entre {} e {} é igual a {}.'.format(n1, n2, n1+n2))

    elif opcao == 2:
        print('A multiplicação entre {} e {} é igual a {}.'.format(n1, n2, n1*n2))

    elif opcao == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print('O maior dos valores digitados é {}.'.format(maior))
    
    elif opcao == 4:
        print('Informe os novos valores: ')
        n1 = int(input('\nPrimeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif opcao == 5:
        print('Finalizando...')

    else:
        print('Opção inválida. Tente novamente.')
    
    sleep(1)
print('Fim do programa. Volte sempre!')