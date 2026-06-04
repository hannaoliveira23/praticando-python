'''
# Tentativa 1
print('~'*40)
print(f'{'CAIXA ELETRÔNICO DA HANNA :D':^40}')
print('~'*40)

valor = int(input('Quanto você deseja sacar? R$'))

num50 = valor // 50
valor = valor % 50

num20 = valor // 20
valor = valor % 20

num10 = valor // 10
valor = valor % 10

num1 = valor // 1
valor = valor % 1

print('Total de cédulas:')
print(f'> {num50} cédulas de R$50,00;\n> {num20} cédulas de R$20,00;\n> {num10} cédulas de R$10,00;\n> {num1} cédulas de R$1,00.')
print('-'*40)
print('Tenha um bom dia e volte sempre! >.<')

# SOLUÇÃO DO VÍDEO:
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)

valor = int(input('Que valor você quer sacar? R$'))

total = valor
céd = 50
totcéd = 0

while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd = 20:
            céd = 10
        elif céd == 10:
            céd = 1

        totcéd = 0

        if total == 0:
            break

print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
'''

# Tentativa 2:
print('-' * 40)
print(f'{'BANCO OLIVEIRA':^40}')
print('-' * 40)

valor = int(input('Quanto você deseja sacar? R$'))
print('Você obterá:')

ced = 50
while True:
    totCed = valor // ced
    valor = valor % ced

    if totCed > 0:
        print(f'> {totCed} cédulas de {ced},00')
    
    if valor == 0:
        break

    if ced == 50:
        ced = 20
    elif ced == 20:
        ced = 10
    elif ced == 10:
        ced = 1
    
print('-' * 40)
print('Tenha um bom dia e volte sempre!')