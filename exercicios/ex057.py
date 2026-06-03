sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while not(sexo == 'M' or sexo == 'F'):
    sexo = str(input('Dado inválido. Digite novamente: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))