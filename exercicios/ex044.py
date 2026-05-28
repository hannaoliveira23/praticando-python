precoNormal = float(input('Digite o preço do produto: '))
formaPagamento = int(input('\nEscolha uma forma de pagamento (digite o número correspondente à opção):\n' \
                           '1. À vista em dinheiro/pix (10% de desconto)\n' \
                           '2. À vista no cartão (5% de desconto)\n' \
                           '3. Parcelado em até 2x no cartão (preço normal)\n' \
                           '4. Parcelado em 3x ou mais no cartão (20% de juros)\n> '))

if formaPagamento == 1:
    precoFinal = precoNormal - (precoNormal*10/100)
    print('\nO preço final do produto será R${:.2f}.\n'.format(precoFinal))

elif formaPagamento == 2:
    precoFinal = precoNormal - (precoNormal*5/100)
    print('\nO preço final do produto será R${:.2f}.\n'.format(precoFinal))

elif formaPagamento == 3:
    print('\nSua conta foi parcelada em 2x de R${:.2f} (SEM JUROS).'.format(precoNormal/2))
    print('O preço final do produto será R${:.2f}.\n'.format(precoNormal))

elif formaPagamento == 4:
    numParcelas = int(input('\nEm quantas parcelas você deseja dividir? '))
    
    precoFinal = precoNormal + (precoNormal*20/100)
    parcelaMensal = precoFinal / numParcelas

    print('\nSua conta foi parcelada em {}x de R${:.2f} (COM JUROS).'.format(numParcelas, parcelaMensal))
    print('O preço final do produto será R${:.2f}.\n'.format(precoFinal))

else:
    print('\nA opção escolhida não corresponde a nenhuma forma apresentada.\n')