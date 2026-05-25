nome = input('Digite o seu nome: ').strip()

print('Maiúsculas:', nome.upper())
print('Minúsculas:', nome.lower())

nomeDiv = nome.split()
nomeSemEspacos = ''.join(nomeDiv)
# Ou: len(nome) - nome.count(' ')

print('Quantidade de letras no total, sem considerar espaços:', len(nomeSemEspacos))
print('Quantidade de letras do primeiro nome:', len(nomeDiv[0])) # ou nome.find(' ')