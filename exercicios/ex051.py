an = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for i in range(0,10):
    print('{} '.format(an), end='')
    an += r
print()

# SOLUÇÃO DO VÍDEO
# primeiro = int(input('Primeiro termo: '))
# razao = int(input('Razão: '))
# decimo = primeiro + (10-1)*razão
# for c in range(primeiro, decimo + razao, razao)
#     print('{} '.format(c), end = '-> ')
# print('ACABOU')