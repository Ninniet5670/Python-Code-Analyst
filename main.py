from data_processing import PySmells
import os


os.system(f"pylint --msg-template='{{msg_id}}::{{msg}}' teste >> pylint_errors.txt")
os.system(f"pycodestyle --statistics -qq teste >> pep8_errors.txt")

print(PySmells('pylint_errors.txt').insigth_pylint())
print(PySmells('pylint_errors.txt').insigth_pylint(True))
print(PySmells('pylint_errors.txt').pylint_score())
print(PySmells('pep8_errors.txt').pep8_insigth())
