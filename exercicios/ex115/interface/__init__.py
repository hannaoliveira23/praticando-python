def linha(tam = 34):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(f'{txt:^34}')
    print(linha())


def leiaInt(f):
    while True:
        try:
            a = int(input(f))
        except:
            print(f'{'\033[31m'}ERRO: Digite um número inteiro válido.{'\033[m'}')
        else:
            return a


def menu(lista):
    cabecalho('MENU DE CADASTRO')
    c = 1
    for item in lista:
        print(f'{c}. {item}')
        c += 1
    print(linha())
    opc = leiaInt('> ')
    return opc
