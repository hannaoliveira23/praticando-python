def ficha(nome, qtdeGols):
    """
    Mostra a ficha de um jogador (seu nome e quantidade de gols).
    :param nome: O nome do jogador.
    :param qtdeGols: A quantidade de gols feita pelo jogador.
    """
    if nome == '':
        nome = '<desconhecido>'

    if qtdeGols == '' or not qtdeGols.isnumeric():
        qtdeGols = 0

    print(f'O jogador {nome} fez {qtdeGols} gol(s) no campeonato.')

nome = str(input('Nome do jogador: '))
gols = str(input('Quantidade de gols: '))

ficha(nome, gols)