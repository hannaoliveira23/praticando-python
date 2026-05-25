nome = str(input('Digite um nome: ')).strip()
dividido = nome.split()
print('O primeiro nome é {}.'.format(dividido[0]))
print('O último nome é {}.'.format(dividido[len(dividido)-1])) 