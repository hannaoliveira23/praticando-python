def dobro(valor):
    return valor * 2


def metade(valor):
    return valor/2


def aumentar(valor, percentual):
    return valor + (valor * percentual / 100)


def diminuir(valor, percentual):
    return valor - (valor * percentual / 100)


def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')
