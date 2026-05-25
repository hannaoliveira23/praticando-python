d = float(input('Digite a distância da viagem, em Km: '))

if d <= 200:
    preco = d * 0.5
else:
    preco = d * 0.45

# OU: preco = d * 0.5 if d <= 200 else d * 0.45

print('O preço da viagem é R${}.'.format(preco))