import pandas as pd
import numpy as np


np.random.seed(100)

indice1 = ['Nível1', 'Nível1', 'Nível1', 'Nível2', 'Nível2', 'Nível2']
indice2 = ['Subnível1', 'Subnível2', 'Subnível3', 'Subnível1', 'Subnível2', 'Subnível3']

indice3 = list(zip(indice1, indice2))
indice3 = pd.MultiIndex.from_tuples(indice3)

dados = np.random.randn(6, 2)

print(indice3)

base = pd.DataFrame(
    data=dados,
    index=indice3,
    columns=['Indicador1', 'Indicador2']
)

base.index.names = ['Níveis', 'Subníveis']

base.to_csv('./indices_multiniveis.csv', sep=';')

print(base)

print(base.loc['Nível2'].loc['Subnível2'])

print(base.xs('Nível2'))

