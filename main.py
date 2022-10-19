import os


arq = open('pep8_errors.txt', 'a')


def recursive_dir(code):
    for file in os.listdir(os.curdir):
        if os.path.isdir(file):
            os.chdir(file)
            recursive_dir(code)
        else:
            if file.split('.')[-1] == 'py':
                os.system(
                    f'{code} {file} >> auxiliar.txt')

                with open('auxiliar.txt', 'r') as arqq:
                    arq.write(arqq.read())
                os.remove('auxiliar.txt')
    os.chdir('..')


choice = input('''
Escolha uma opção:
[1] Checar erros de pep8
[2] Checar erros de pylint
[3] Rodar autopep recursivamente no diretório atual
[0] Sair
Digite: ''')

if choice == '1':
    recursive_dir('pycodestyle --first')
elif choice == '2':
    recursive_dir('pylint')
elif choice == '3':
    recursive_dir('autopep8 --in-place --aggressive --aggressive')
elif choice == '0':
    exit()

arq.close()
