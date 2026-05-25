from math import sqrt, pow

ca = float(input('Digite o comprimento do cateto adjacente: '))
co = float(input('Digite o comprimento do cateto oposto: '))

hi = sqrt(pow(ca, 2) + pow(co, 2))
# hi = hypot(co, ca)

print('O comprimento da hipotenusa é {}.'.format(hi))