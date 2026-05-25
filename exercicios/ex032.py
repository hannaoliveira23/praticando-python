from datetime import date
ano = int(input('Digite um ano (coloque 0 para representar o ano atual): '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('O ano {} é bissexto.'.format(ano))
        else:
            print('O ano {} NÃO é bissexto.'.format(ano))
    else:
        print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} NÃO é bissexto.'.format(ano))

# ou
# if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
#     print('O ano é bissexto.')
# else:
#     print('O ano NÃO é bissexto.')