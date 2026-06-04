somaCompra = contCaros = precoMaisBarato = contProdutos = 0
produtoMaisBarato = ''

print('-'*40)
print(f'{'CALCULADORA DE PREÇOS':^40}')
print('-'*40)

while True:
    nome = str(input('\nDigite o nome do produto: '))
    preco = float(input('Digite o preço do produto: R$'))
    contProdutos += 1

    if contProdutos == 0 or preco < precoMaisBarato:
        precoMaisBarato = preco
        produtoMaisBarato = nome
    
    somaCompra += preco

    if preco > 1000:
        contCaros += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('\nDeseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('\nFINALIZANDO...')
print(f'Sua compra resultou em R${somaCompra:.2f}.')
print(f'{contCaros} produtos custaram mais de R$1000.00.')
print(f'O produto mais barato foi o {produtoMaisBarato}, que custou R${precoMaisBarato:.2f}.')