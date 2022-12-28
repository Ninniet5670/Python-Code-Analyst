from data_processing import PySmells
import os

def centralize(word):
    print(f'{word:-^40}')

dir = input('The dir to be analyzed: ')

os.system(f"pylint --msg-template='{{msg_id}}::{{msg}}' {dir} > pylint_errors.txt")
os.system(f"pycodestyle --statistics -qq {dir} > pep8_errors.txt")
os.system(f"mypy --check-untyped-defs {dir} > mypy_errors.txt")

centralize(' Pylint Errors ')
print(PySmells('pylint_errors.txt').pylint_insigth())

centralize(' Pylint Errors by Type ')
print(PySmells('pylint_errors.txt').pylint_insigth(True))

centralize(' Pylint Program Score ')
print(PySmells('pylint_errors.txt').pylint_score())

centralize(' Pep8 Errors ')
print(PySmells('pep8_errors.txt').pep8_insigth())

centralize(' MyPy Errors ')
print(PySmells('mypy_errors.txt').mypy_insigth())
