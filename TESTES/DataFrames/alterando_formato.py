import numpy as np
import pandas as pd


base = pd.DataFrame(
    data=np.random.randn(6, 5),
    index=np.arange(1, 7),
    columns=['a', 'b', 'c', 'd', 'e']
)

print(f'{base}\n')

base = pd.melt(base)

print(base)
