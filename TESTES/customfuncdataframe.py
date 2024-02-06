import numpy as np
import pandas as pd


def quadrado(x):
    return x ** 2
    


np.random.seed(100)

dados = np.random.randn(5, 3)
indices = np.arange(1, 6)
colunas = ['A', 'B', 'C']

base = pd.DataFrame(
    data=dados,
    index=indices,
    columns = colunas
)

print(base.apply(quadrado))

print(base.apply(lambda x: x ** 2))
