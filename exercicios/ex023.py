num = input('Digite um número inteiro entre 0 e 9999: ')

# Ainda não dá para tratar com string sem os conceitos de estruturas condicionais!

print('TRATANDO O NÚMERO COMO INT')
num = int(num)

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print('Unidade: {}\nDezena:  {}\nCentena: {}\nMilhar:  {}'.format(unidade, dezena, centena, milhar))