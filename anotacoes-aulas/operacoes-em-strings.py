frase = 'Curso em Vídeo Python'

# FATIAMENTO
print('Fatiamento de strings: ')
print(frase[9]) # Imprime a letra na posição 9
print(frase[9:14]) # Imprime da posição 9 até a posição 13 (14-1)
print(frase[9:21]) # Imprime da posição 9 até a posição 20 (21-1)
print(frase[9:21:2]) # Imprime da posição 9 até a posição 20, pulando de 2 em 2
print(frase[:5]) # Imprime da posição 0 até a posição 4
print(frase[15:]) # Imprime da posição 15 até o final da string
print(frase[9::3]) # Imprime da posição 9 até o final da string, pulando de 3 em 3
print(frase[::2]) # Imprime toda a string, pulando de 2 em 2

# ANÁLISE
print('\nAnálise da string: ')
print(len(frase)) # Imprime o comprimento da string
print(frase.count('o')) # Conta quantas vezes a letra 'o' aparece na string
print(frase.count('o', 0, 13)) # Conta quantas vezes a letra 'o' aparece na string, da posição 0 até a posição 12 (13-1)
print(frase.find('deo')) # Encontra a posição onde começa a string 'deo'
print(frase.find('Android')) # Retorna -1, pois a string 'Android' não foi encontrada
print('Curso' in frase) # Retorna True, pois a string 'Curso' está presente na string 'frase'

# TRANSFORMAÇÃO
print('\nTransformação da string: ')
print(frase.replace('Python', 'Android')) # Substitui a string 'Python' pela string 'Android'
print(frase.upper()) # Converte a string para maiúscula
print(frase.lower()) # Converte a string para minúscula
print(frase.capitalize()) # Converte a primeira letra da string inteira para maiúscula e as demais para minúscula
print(frase.title()) # Converte a primeira letra de cada palavra para maiúscula
print(frase.strip()) # Remove os espaços em branco no início e no final da string
print(frase.rstrip()) # Remove os espaços em branco no final da string
print(frase.lstrip()) # Remove os espaços em branco no início da string

# DIVISÃO
print('\nDivisão da string: ')
print(frase.split()) # Divide a string em uma lista de palavras
print(frase.split()[0]) # Imprime a primeira palavra da string
print(frase.split()[2]) # Imprime a terceira palavra da string

# JUNÇÃO
print('-'.join(frase.split())) # Junta os caracteres da string, colocando um '-' entre eles