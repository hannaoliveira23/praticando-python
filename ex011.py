b = float(input('Digite a largura da parede: '))
h = float(input('Digite a altura da parede: '))

area = b*h
# 1l de tinta = 2m^2
tinta = area/2

print('Para pintar a parede inteira, você precisa de {} litro(s) de tinta.'.format(tinta))