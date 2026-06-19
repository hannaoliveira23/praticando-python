def dobro(valor, formatacao=False):
    if formatacao:
        return moeda(valor * 2)
    else:
        return valor * 2


def metade(valor, formatacao=False):
    if formatacao:
        return moeda(valor/2)
    else:
        return valor/2


def aumentar(valor, percentual, formatacao=False):
    if formatacao:
        return moeda(valor + (valor * percentual / 100))
    else:
        return valor + (valor * percentual / 100)


def diminuir(valor, percentual, formatacao=False):
    if formatacao:
        return moeda(valor - (valor * percentual / 100))
    else:
        return valor - (valor * percentual / 100)


def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')


def resumo(valor, aumento, reducao):
    print('-'*30)
    print(f'{'RESUMO DO VALOR':^30}')
    print('-'*30)

    print(f'{f'Preço analisado:':<20}{f'{moeda(valor)}':>10}')
    print(f'{f'Dobro do preço:':<20}{f'{dobro(valor, True)}':>10}')
    print(f'{f'Metade do preço:':<20}{f'{metade(valor, True)}':>10}')
    print(f'{f'{aumento}% de aumento:':<20}{f'{aumentar(valor, aumento, True)}':>10}')
    print(f'{f'{reducao}% de redução:':<20}{f'{diminuir(valor, reducao, True)}':>10}')

    print('-'*30)
