import pandas as pd
import numpy as np
from random import randint

indices = np.arange(1, 11)
numeros = np.array(
    [randint(1, 100) for i in range(10)]
)

serie = pd.Series(
    data=numeros,
    index=indices
)

print(serie.index)
