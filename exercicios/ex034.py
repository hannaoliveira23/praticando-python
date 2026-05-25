salario = float(input('Digite o salário: R$'))

if salario > 1250.00:
    salario = salario + (salario*10/100)
else:
    salario = salario + (salario*15/100)

print('O salário com aumento será igual a R${:.2f}.'.format(salario))