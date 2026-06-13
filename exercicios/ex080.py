lista = []
for c in range(0,5):
    valor = int(input('Digite um número: '))

    if c == 0:
        lista.append(valor)
        print('Primeiro elemento adicionado ao final da lista!')
    else:
        cont = 0
        for num in lista:
            if valor > num:
                cont += 1
        lista.insert(cont, valor)
        print(f'Elemento adicionado na posição {cont}.')
print(f'Lista final: {lista}')