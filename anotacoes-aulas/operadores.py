# Ordem de precedência:
# 1. Parênteses
# 2. Potência
# 3. Multiplicação, divisão, divisão inteira (//), módulo (%)
# 4. Soma, subtração

# potência: 5**2 = pow(5,2)
# raiz quadrada: 25**(1/2)
# raiz cúbica: 25**(1/3)

print('->'*3, end=' ') 

nome = input('Qual é seu nome? ')
print('Prazer em te conhecer, {}!'.format(nome))
print('Prazer em te conhecer, {:20}!'.format(nome))
print('Prazer em te conhecer, {:>20}!'.format(nome))
print('Prazer em te conhecer, {:^20}!'.format(nome))
print('Prazer em te conhecer, {:-^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
p = n1 * n2
e = n1**n2
d = n1/n2
di = n1//n2
print('A soma vale {}, a divisão {}, a divisão inteira {}, o produto {} e a potência {}.'.format(s,d,di,p,e))