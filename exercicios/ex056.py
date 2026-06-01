somaIdade = 0
idadeHomemMaisVelho = 0
nomeHomemMaisVelho = ''
contMulheres = 0

for i in range(0,4):
    print()
    print('-'*20)
    print('PESSOA {}'.format(i+1))
    print('-'*20)

    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo (M/F): ')).strip().upper()

    somaIdade += idade

    if sexo == 'M':
        if idade > idadeHomemMaisVelho:
            idadeHomemMaisVelho = idade
            nomeHomemMaisVelho = nome
    elif sexo == 'F':
        if idade < 20:
            contMulheres += 1

print('\nA média de idade do grupo é {:.2f}.'.format(somaIdade/4))
if idadeHomemMaisVelho <= 0:
    print('Nenhuma entrada era correspondente a um homem.')
else:
    print('O nome do homem mais velho é {}.'.format(nomeHomemMaisVelho))
print('{} mulheres têm menos de 20 anos.'.format(contMulheres))