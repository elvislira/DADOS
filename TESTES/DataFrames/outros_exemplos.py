import numpy as np
import pandas as pd

np.random.seed(100)

dados = np.random.randn(6, 5)
indices = range(1, 7)
colunas = ['A', 'B', 'C', 'D', 'E']

base = pd.DataFrame(
    data=dados,
    index=indices,
    columns=colunas
)

soma = base['A'] + base['B'] + base['C'] + base['D'] + base['E']

base['Soma'] = soma

# base.drop('C', axis=1, inplace=True)

# del base['E']

# base.sort_values(by='A', inplace=True)

print(base)

# print(base.iloc[1:5, 1:4])

print(round(base,0))


