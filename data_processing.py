from collections import Counter


def pep8_data_process():
    erros = []

    with open('pep8_errors.txt', 'r+') as arq:
        arqq = arq.read()

    arqq = arqq.split('\n')
    arqq.pop()
    for i, erro in enumerate(arqq):
        arqq[i] = str(erro.split(': ')[1:][0]).split(',')

    for erro in arqq:
        try:
            x, y = erro[0].split()[0], int(erro[1].split()[-1])
        except:
            x, y = erro[0].split()[0], 1
        
        for i in range(y):
            erros.append(x)

    return dict(Counter(erros))


def pylint_data_process():
    with open('pylint_errors.txt', 'r+') as arq:
        arqq = arq.read()

    arqq = arqq.split('\n')
    for i, erro in enumerate(arqq):
        if '*' in arqq[i] or arqq[i] == '':
            arqq.pop(i)

    print(arqq)

pylint_data_process()
