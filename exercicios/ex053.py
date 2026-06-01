frase = str(input('Digite uma frase (sem acentos): '))
frase = frase.replace(' ', '').lower()

tamFrase = len(frase)

palindromo = True
for a in range(0, tamFrase//2):
    x = frase[a]
    y = frase[tamFrase-1]

    if x != y:
        palindromo = False

    tamFrase -= 1

if palindromo:
    print('{}A frase É palíndromo.{}'.format('\033[32m', '\033[m'))
else:
    print('{}A frase NÃO É palíndromo.{}'.format('\033[31m', '\033[m'))

# SOLUÇÃO DO VÍDEO:
# frase = str(input('Digite uma frase: ')).strip().upper()
# palavras = frase.split()
# junto = ''.join(palavras)
# inverso = ''
# for letra in range(len(junto) - 1, -1, -1):
#     inverso += junto[letra]
# print('O inverso de {} é {}'.format(junto, inverso))
# if inverso == junto:
#     print('Temos um palíndromo!')
# else:
#     print('A frase digitada não é um palíndromo!')

# As linhas 25 a 27 podem ser substituídas ainda por inverso = junto[::-1]