s = 0
c = 0
for i in range(0,6):
    num = int(input('Digite um número ({} números restantes): '.format(6-i)))
    if num % 2 == 0:
        s += num
        c += 1
    
print('A soma dos {} números pares digitados é {}.'.format(c, s))