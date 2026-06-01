s = 0
for i in range(1,500):
    if i % 2 > 0 and i % 3 == 0:
        s += i

print('A soma de todos os números ímpares que são múltiplos ' \
      'de 3 no intervalo de 1 a 500 é igual a {}.'.format(s))

# VERSÃO OTIMIZADA:
# soma = 0
# cont = 0
# for i in range(1,501,2):
#     if i % 3 == 0:
#         soma += i
#         cont += 1
# print('A soma de todos os {} valores solicitados é {}.'.format(cont, soma))