peso = float(input('Digite seu peso (em Kg): '))
alturaCM = int(input('Digite sua altura (em cm): '))

alturaM = (float)(alturaCM / 100) 

imc = (float)(peso/(alturaM**2))

if imc < 18.5:
    print('O IMC foi igual a {:.2f}. Você está ABAIXO DO PESO.'.format(imc))

elif imc < 25:
    print('O IMC foi igual a {:.2f}. Você está no PESO IDEAL.'.format(imc))

elif imc < 30:
    print('O IMC foi igual a {:.2f}. Você está com SOBREPESO.'.format(imc))

elif imc < 40:
    print('O IMC foi igual a {:.2f}. Você está com OBESIDADE.'.format(imc))

else:
    print('O IMC foi igual a {:.2f}. Você está com OBESIDADE MÓRBIDA.'.format(imc))