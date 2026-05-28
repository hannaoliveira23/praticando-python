from datetime import date

dia = int(input('Digite o dia de nascimento do atleta: '))
mes = int(input('Digite o mes de nascimento do atleta: '))
ano = int(input('Digite o ano de nascimento do atleta: '))

dataNasc = date(ano, mes, dia)
dataAtual = date.today()

idade = dataAtual.year - dataNasc.year
fez_aniversario = (dataAtual.month, dataAtual.day) >= (dataNasc.month, dataNasc.day)

if not fez_aniversario:
    idade -= 1

if idade <= 9:
    print('A categoria do atleta é MIRIM.')

elif idade <= 14:
    print('A categoria do atleta é INFANTIL.')

elif idade <= 19:
    print('A categoria do atleta é JÚNIOR.')

elif idade <= 25:
    print('A categoria do atleta é SÊNIOR.')

else:
    print('A categoria do atleta é MASTER.')