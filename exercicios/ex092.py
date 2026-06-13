from datetime import date

pessoa = dict()
pessoa['Nome'] = str(input('Nome: '))

anoNasc = int(input('Ano de nascimento: '))
anoAtual = date.today().year
#          datetime.now().year
pessoa['Idade'] = anoAtual - anoNasc

pessoa['CTPS'] = int(input('CTPS: '))
if pessoa['CTPS'] != 0:
    anoContratacao = int(input('Ano de contratação: '))
    pessoa['Ano de contratação'] = anoContratacao
    pessoa['Salário'] = float(input('Salário: R$'))
    pessoa['Idade de Aposentadoria'] = anoContratacao - anoNasc + 35

print('\nRESUMO DAS INFORMAÇÕES: ')
for c, v in pessoa.items():
    print(f'    > {c}: {v}')