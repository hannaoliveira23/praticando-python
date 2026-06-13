def area(l,c):
    print(f'A área de um terreno com dimensões {l:.1f}m² por {c:.1f}m² é de {l*c:.1f}m².')


print('DIMENSÕES:')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c)