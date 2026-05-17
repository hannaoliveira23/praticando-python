dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos Km rodados? '))

precoTotal = (60*dias) + (0.15*km)

print('O total a pagar pelo aluguel é R${:.2f}.'.format(precoTotal))
