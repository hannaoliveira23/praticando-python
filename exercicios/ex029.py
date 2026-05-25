vel = float(input('Qual é a velocidade do carro? '))

if vel > 80.0:
    ult = vel - 80
    multa = ult * 7
    print('Você ultrapassou o limite de 80Km/h. A multa a ser paga é de R${:.2f}.'.format(multa))

print('Tenha um bom dia. Dirija com segurança!')