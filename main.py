from data_processing import PySmells
import os


# para mais de um projeto
# for file in os.listdir(os.curdir):
#     if os.path.isdir(file) and file != '.git':
#         os.system(f"pylint --msg-template='{{msg_id}}:{{msg}}' {file} >> {file}_pylint_errors.txt")
#         os.system(f"pycodestyle --statistics -qq {file} >> {file}_pep8_errors.txt")


os.system(f"pylint --msg-template='{{msg_id}}::{{msg}}' teste >> pylint_errors.txt")
os.system(f"pycodestyle --statistics -qq teste >> pep8_errors.txt")

print(PySmells('pylint_errors.txt').insigth_pylint())
print(PySmells('pylint_errors.txt').insigth_pylint(True))
print(PySmells('pylint_errors.txt').pylint_score())
