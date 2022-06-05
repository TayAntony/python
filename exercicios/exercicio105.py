def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    n: uma ou mais notas dos alunos (aceita várias)
    sit: valor opcional, indicando se deve ou não adicionar a situação do aluno de acordo com a média (m)
    return: dicionário com várias informações sobre as notas dos alunos (média, mínima e máxima)
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(8.2, 6.7, 9, 7.5, 10,  sit=True)
print(resp)
help(notas)