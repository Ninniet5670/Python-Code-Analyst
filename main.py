import os


arq = open('lista_erros.txt', 'a')
def recursive_dir(code):
    for file in os.listdir(os.curdir):
        if os.path.isdir(file):
            os.chdir(file)
            recursive_dir(code)
            print(file)
        else:
            if file.split('.')[-1] == 'py':
                os.system(
                    f'{code} {file} >> aux.txt')
                
                with open('aux.txt', 'r') as arqq:
                    arq.write(arqq.read())
                os.remove('aux.txt')
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
