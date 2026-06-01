from datetime import date

contMaior = 0
for i in range(0,7):
    ano = int(input('Digite o ano de nascimento ({} restantes): '.format(7-i)))
    atual = date.today().year

    if atual - ano >= 21:
        contMaior += 1
print('{} pessoas atingiram a maioridade. {} ainda são de menor.'.format(contMaior, 7 - contMaior))