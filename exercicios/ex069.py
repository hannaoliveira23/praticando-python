contMaioridade = contHomens = contMulheres = 0
while True:
    print('-'*40)
    print(f'{'CADASTRANDO UMA PESSOA':^40}')
    print('-'*40)

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [F/M]: ')).strip().upper()[0]
    
    idade = int(input('Digite a idade: '))

    if idade >= 18:
        contMaioridade += 1
    if sexo == 'M':
        contHomens += 1
    if sexo == 'F' and idade < 20:
        contMulheres += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('\nDeseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('\nFIM DO CADASTRO.')
print(f'Foram cadastradas:\n > {contMaioridade} pessoas com mais de 18 anos;')
print(f' > {contHomens} homens; e\n > {contMulheres} mulheres com menos de 20 anos.')