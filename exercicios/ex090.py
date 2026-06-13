aluno = dict()
aluno['Nome'] = str(input('Digite o nome do aluno: '))
aluno['Média'] = float(input(f'Qual é a média de {aluno["Nome"]}? '))
aluno['Situação'] = ('Reprovado' if aluno['Média'] < 5.0 else 'Recuperação' if 5.0 <= aluno['Média'] < 7.0 else 'Aprovado')
print('\nRESUMO DAS INFORMAÇÕES:')
for c, v in aluno.items():
    print(f'{c}: {v}.')