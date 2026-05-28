print('')
print('{}Análise de aprovação de empréstimo bancário...{}'.format('\033[34m', '\033[m'))
valorCasa = float(input('{}Digite o valor da casa: R${}'.format('\033[34m', '\033[m')))
salario = float(input('{}Digite o seu salário: R${}'.format('\033[34m', '\033[m')))
tempo = int(input('{}Em quantos anos você vai pagar? {}'.format('\033[34m', '\033[m')))

prestacaoMensal = (float)(valorCasa/(tempo*12))
minimo = salario*30/100 # 30% do salário

print('')

if prestacaoMensal <= minimo:
    print('{}O empréstimo foi APROVADO.{}'.format('\033[32m', '\033[m'))
    print('{}A prestação mensal será de R${:.2f}.{}'.format('\033[32m', prestacaoMensal, '\033[m'))

else:
    print('{}O empréstimo foi NEGADO. A prestação mensal ultrapassa 30% do seu salário atual.{}'.format('\033[31m', '\033[m'))
    print('{}A prestação mensal foi igual a R${:.2f}.{}'.format('\033[31m', prestacaoMensal, '\033[m'))

print('')

# PROGRAMA SEM CORES
# print('Análise de aprovação de empréstimo bancário...'))
# valorCasa = float(input('{}Digite o valor da casa: R${}')))
# salario = float(input('{}Digite o seu salário: R${}')))
# tempo = int(input('Em quantos anos você vai pagar? '))

# prestacaoMensal = (float)(valorCasa/tempo)
# minimo = salario*30/100 # 30% do salário

# if prestacaoMensal <= minimo:
#     print('O empréstimo foi APROVADO.')
#     print('A prestação mensal será de R${:.2f}.'.format(prestacaoMensal))

# else:
#     print('O empréstimo foi NEGADO. A prestação mensal ultrapassa 30% do seu salário atual.')
#     print('A prestação mensal foi igual a R${:.2f}.'.format(prestacaoMensal))