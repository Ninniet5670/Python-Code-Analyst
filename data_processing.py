from collections import Counter

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

print(dict(Counter(erros)))
