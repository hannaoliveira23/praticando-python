expressão = str(input('Digite uma expressão matemática: '))

pilha = []
inválida = False
for caracter in expressão:
    if caracter == '(':
        pilha.append(caracter)
    if caracter == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            inválida = True
            break

if len(pilha) == 0 and inválida == False:
    print('A expressão é VÁLIDA!')
else:
    print('A expressão é INVÁLIDA!')