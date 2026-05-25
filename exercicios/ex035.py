l1 = float(input('Digite um comprimento: '))
l2 = float(input('Digite outro comprimento: '))
l3 = float(input('Digite o último comprimento: '))

if (l1 + l2) > l3 and (l2 + l3) > l1 and (l1 + l3) > l2:
    print('As três medidas digitadas podem formar um triângulo.')
else:
    print('As três medidas digitadas NÃO podem formar um triângulo.')