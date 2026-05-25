frase = str(input('Digite uma frase: ')).strip()
frase = frase.upper()

print('Contagem de "a"s:', frase.count('A'))

prim = frase.find('A')
ult = frase.rfind('A')
print('O primeiro "a" aparece na posição {} e o último na {}.'.format(prim, ult))