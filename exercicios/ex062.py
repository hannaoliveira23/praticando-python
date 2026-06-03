a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
qtdeTermos = int(input('Quantos termos você deseja? '))

cont = 0
total = qtdeTermos

while qtdeTermos > 0:
    while cont < total:
        print(a1 + r*cont, end=' ')
        cont += 1

    qtdeTermos = int(input('\nVocê deseja obter mais quantos termos? '))
    total += qtdeTermos

'''
SOLUÇÃO DO VÍDEO
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
'''