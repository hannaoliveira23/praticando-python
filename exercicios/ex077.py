palavras = ('wedding', 'faith', 'unbreakable', 'blood', 'funky', 'myxomatosis', 'remember', 'children')

for palavra in palavras:
    print(f'\nA palavra {palavra.upper()} tem as vogais ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
print()