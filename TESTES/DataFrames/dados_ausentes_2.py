import numpy as np
import pandas as pd


dados = {
    '1º Semestre': [8.2, 8.0, np.nan],
    '2º Semestre': [7.7, np.nan, 8.0],
    '3º Semestre': [7.9, np.nan, np.nan]
}

indices = ['Nota 1', 'Nota 2', 'Nota 3']

boletim = pd.DataFrame(
    data=dados,
    index=indices
)

print(f'{boletim}\n')

boletim['1º Semestre'] = boletim['1º Semestre'].fillna(boletim['1º Semestre'].mean())
boletim['2º Semestre'] = boletim['2º Semestre'].fillna(boletim['2º Semestre'].mean())
boletim['3º Semestre'] = boletim['3º Semestre'].fillna(boletim['3º Semestre'].mean())

print(boletim)
