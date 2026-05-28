from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))

idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')

elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))

elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))

'''
MINHA SOLUÇÃO ANTERIOR (USANDO DIAS)

from datetime import date

dia = int(input('Digite o dia de seu nascimento: '))
mes = int(input('Digite o mês de seu nascimento: '))
ano = int(input('Digite o ano de seu nascimento: '))

dataAlist = date(ano + 18, mes, dia)
dataAtual = date.today()

diferenca = dataAlist - dataAtual
diasPositivos = abs(diferenca.days)

if diferenca.days > 0:
    print('Faltam {} dias para o seu alistamento.'.format(diasPositivos))

elif diferenca.days < 0:
    print('Já se passaram {} dias da sua data de alistamento ({})!'.format(diasPositivos, dataAlist))

else:
    print('Você deve se alistar hoje!!')
'''