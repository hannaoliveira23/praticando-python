num = int(input('Digite um número inteiro: '))
base = int(input('Escolha a base de conversão:\n1. Binário\n2. Octal\n3. Hexadecimal\n> '))

if base == 1:
    numBin = bin(num)[2:]
    print('{} em binário é igual a {}.'.format(num, numBin))

elif base == 2:
    numOct = oct(num)[2:]
    print('{} em octal é igual a {}.'.format(num, numOct))

elif base == 3:
    numHex = hex(num)[2:]
    print('{} em hexadecimal é igual a {}.'.format(num, numHex))

else:
    print('A base escolhida não corresponde a nenhuma das opções oferecidas.')