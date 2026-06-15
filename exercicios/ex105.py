def notas(*notas, sit=False):
    """
    Retorna uma análise das notas de vários alunos.
    :param *notas: As notas a serem analisadas. A quantidade de notas é indefinida.
    :param sit (opcional): Adiciona no dicionário retornado a situação da turma.
    :return: Retorna o dicionário que reúne todas as informações sobre as notas (total de notas, maior nota, menor nota, média da turma).
    """
    overview = dict()
    cont = soma = 0
    maior = menor = notas[0]
    for i in notas:
        if maior < i:
            maior = i
        if menor > i:
            menor = i
        cont += 1
        soma += i
    overview['total'] = cont
    overview['maior'] = maior
    overview['menor'] = menor
    overview['média'] = soma/cont
    
    if sit:
        overview['situação'] = 'RUIM' if overview['média'] < 5.0 else 'RAZOÁVEL' if overview['média'] < 7.0 else 'BOA'

    return overview


print(notas(10.0, 5.6, 8.9, 3.4, 7.6, 2.2, 4.3, sit=True))

'''
PARTE DA SOLUÇÃO DO VÍDEO
def notas(*n, sit=False):
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)]
    r['média'] = sum(n)/len(n)
'''