def voto(anoNasc):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - anoNasc
    
    print(f'Com {idade} anos, o voto é ', end='')

    if idade < 16:
        print('NEGADO.')
    elif idade < 18 or idade > 69:
        print('OPCIONAL.')
    else:
        print('OBRIGATÓRIO.')


voto(int(input('Digite o ano de nascimento: ')))