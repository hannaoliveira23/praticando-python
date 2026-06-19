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
