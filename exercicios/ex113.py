def leiaInt(f):
    """
    Semelhante ao input, porém só aceita valores numéricos inteiros.
    :param f: Frase que será mostrada ao usuário.
    :return: O número inteiro que foi digitado. A função só irá retornar algo quando for digitado um número inteiro válido.
    """
    while True:
        try:
            a = int(input(f))
        except:
            print(f'{'\033[31m'}ERRO: Digite um número inteiro válido.{'\033[m'}')
        else:
            return a

def leiaFloat(f):
    """
    Semelhante ao input, porém só aceita valores numéricos reais.
    :param f: Frase que será mostrada ao usuário.
    :return: O número real que foi digitado. A função só irá retornar algo quando for digitado um número real válido.
    """
    while True:
        try:
            a = float(input(f))
        except:
            print(f'{'\033[31m'}ERRO: Digite um número real válido.{'\033[m'}')
        else:
            return a

m = leiaInt('Digite um número inteiro: ')
n = leiaFloat('Digite um número real: ')
print(f'O número inteiro digitado foi {m} e o real foi {n}.')