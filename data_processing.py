import pandas as pd


class PySmells:
    def __init__(self, file):
        self.file = file

    def insigth_pylint(self, count_by_type=False):
        ''''''
        error_code = []

        with open(self.file, 'r+') as _:
            arq = _.readlines()

        for i in arq:
            try:
                if count_by_type:
                    x, _ = i.split('::')[0][0], i.split('::')[1]
                else:
                    x, _ = i.split('::')[0], i.split('::')[1]
                    
                error_code.append(x)
            except BaseException:
                continue

        return pd.Series(error_code).value_counts()

    def pylint_score(self):
        with open(self.file, 'r+') as _:
            arq = _.readlines()
            while '\n' in arq:
                arq.remove('\n')

        return arq[-1].split('/')[0].split()[-1]
