import os


def recursive_dir():
    for file in os.listdir(os.curdir):
        if os.path.isdir(file):
            os.chdir(file)
            recursive_dir()
            print(file)
        else:
            if file.split('.')[-1] == 'py':
                os.system(
                    f'autopep8 --in-place --aggressive --aggressive {file}')
    os.chdir('..')


choice = input('''
Escolha uma opção:
[1] Checar erros de pep8
[2] Checar erros de pylint
[3] Rodar autopep recursivamente no diretório atual
[0] Sair
Digite: ''')

if choice == '1':
    pass
elif choice == '2':
    pass
elif choice == '3':
    run_autopep()
elif choice == '0':
    exit()
