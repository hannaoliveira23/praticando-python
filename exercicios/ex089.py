# EX.: alunos = [[Maria, [5.0, 6.0], 5.5], [João, [9.0, 7.5], 8.25]]
alunos = list()
while True:
    aluno = list()
    aluno.append(str(input('Nome: ')))

    notas = list()
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))

    media = (notas[0] + notas[1])/2

    aluno.append(notas[:])
    notas.clear()
    aluno.append(media)

    alunos.append(aluno[:])
    aluno.clear()

    resp = str(input('Deseja continuar? [S/N] '))[0]
    if resp in 'Nn':
        break

print()
print('-'*30)
print(f'{'BOLETIM GERAL':^30}')
print('-'*30)
print(f'{'Nº':<5}{'NOME':<15}{'MÉDIA':>10}')
print('-'*30)

for p, a in enumerate(alunos):
    print(f'{p:<5}{a[0]:<15}{a[2]:>10.1f}')
print('-'*30)

while True:
    resp = int(input('Deseja obter as notas de qual aluno? (999 para interromper): '))
    if resp == 999:
        break
    print(f'As notas de {alunos[resp][0]} são {alunos[resp][1]}')
print('Volte sempre!')

'''
A PRIMEIRA PARTE PODE SER FEITA ASSIM:
while True:
    nome = str(input('Nome: ')).strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    
    alunos.append([nome, [nota1, nota2], media])
'''