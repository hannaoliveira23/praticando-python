def fatorial(num, show=False):
    """
    => Calcula o fatorial de um número.
    :param num: O número cujo fatorial será calculado.
    :param show (opcional): Determina se a conta será mostrada ou não.
    :return: O valor do fatorial de num.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end='')
            print(' = ' if c == 1 else ' x ', end='')
        f *= c
    return f

print(fatorial(5, True))