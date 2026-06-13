from random import randint

def sorteia(lst):
    for i in range(0,5):
        lst.append(randint(0,10))
    print(f'Os valores sorteados foram {lst}.')

def somaPar(lst):
    soma = 0
    for valor in lst:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos valores pares da lista é {soma}.')


numeros = list()
sorteia(numeros)
somaPar(numeros)