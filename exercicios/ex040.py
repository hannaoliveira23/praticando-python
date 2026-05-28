n1 = float(input('\nDigite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2)/2

if media < 5.0:
    print(f'O aluno foi {'\033[31m'}REPROVADO{'\033[m'} (média = {media:.2f}).\n')

elif media < 7.0:
    print(f'O aluno está de {'\033[33m'}RECUPERAÇÃO{'\033[m'} (média = {media:.2f}).\n')

else:
    print(f'O aluno foi {'\033[32m'}APROVADO{'\033[m'} (média = {media:.2f}).\n')