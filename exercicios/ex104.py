def leiaInt(f):
    """
    Semelhante ao input, porém só aceita valores numéricos.
    :param f: Frase que será mostrada ao usuário.
    :return: O número que foi digitado. A função só irá retornar algo quando for digitado um número inteiro válido.
    """
    a = input(f)
    while not a.isnumeric():
        print(f'{'\033[31m'}ERRO: Digite um número inteiro válido.{'\033[m'}')
        a = input(f)
    return a

    
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')