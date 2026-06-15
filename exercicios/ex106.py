import pydoc
pydoc.pager = pydoc.plainpager

def formatacao(msg, cor):
    cores = {'amarelo': '\033[30;43m',
             'vermelho': '\033[30;41m',
             'azul': '\033[30;44m',
             'limpa': '\033[m'
            }

    tam = len(msg) + 4
    print(f'{cores[cor]}{"~" * tam}{cores["limpa"]}')
    print(f'{cores[cor]}  {msg}  {cores["limpa"]}')
    print(f'{cores[cor]}{"~" * tam}{cores["limpa"]}')

while True:
    formatacao('SISTEMA DE AJUDA PyHELP', 'amarelo')
    funcao = str(input('\nFunção ou Biblioteca: ')).lower().strip()
    
    if funcao == 'fim':
        formatacao('ATÉ LOGO!', 'vermelho')
        break

    formatacao(f"Acessando o manual do comando '{funcao}'", 'azul')
    print('\033[30;47m', end='')
    help(funcao)
    print('\033[m', end='')