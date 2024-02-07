import numpy as np
import pandas as pd


indices = np.arange(1, 7)
colunas = ['A', 'B', 'C', 'D', 'E']
dados = np.random.randn(6, 5)

base = pd.DataFrame(
    index=indices,
    columns=colunas,
    data=dados
)

print(base)
base[base < 0] = 0.0
print(base)
