import numpy as np
import pandas as pd


dados = {
    'Cidades': ['Recife', 'Salvador', np.nan, 'João Pessoa'],
    'Estados': ['PE', np.nan, 'AL', np.nan],
    'Países': ['Brasil', np.nan, np.nan, 'Brasil']
}

base = pd.DataFrame(dados)

print(f'{base}\n')

print(base.dropna(thresh=2))

base['Países'] = base['Países'].replace({np.nan: 'Brasil'})

print(f'\n{base}')