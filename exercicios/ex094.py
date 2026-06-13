pessoas = list()
pessoa = dict()
while True:
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))

    pessoas.append(pessoa.copy())
    pessoa.clear()

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resp == 'N':
        break

# QUANTAS PESSOAS FORAM CADASTRADAS
print(f'\n> Foram cadastradas {len(pessoas)} pessoas.')

# MÉDIA DE IDADE DO GRUPO
media = 0
for p, i in enumerate(pessoas):
    media += pessoas[p]['idade']
media /= len(pessoas)
print(f'> A média de idade é {media:.2f}.')

# LISTA COM TODAS AS MULHERES
listaMulheres = list()
for pessoa in pessoas:
    if pessoa['sexo'] in 'Ff':
        listaMulheres.append(pessoa)
print(f'> Lista de mulheres: {listaMulheres}')

# LISTA COM TODAS AS PESSOAS COM IDADE ACIMA DA MÉDIA
listaMaisVelhos = list()
for pessoa in pessoas:
    if pessoa['idade'] > media:
        listaMaisVelhos.append(pessoa)
print(f'Lista das pessoas com idade acima da média: {listaMaisVelhos}')