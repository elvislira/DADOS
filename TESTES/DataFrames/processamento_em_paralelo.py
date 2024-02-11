import pandas as pd
import numpy as np
from multiprocessing import Pool
import time


def haversine(df):
    lat1 = 40.671
    lon1 = -73.985
    lat2 = df['latitude'].values
    lon2 = df['longitude'].values

    MiLES = 3959
    
    lat1, lon1, lat2, lon2 = map(np.deg2rad, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    total_miles = MiLES * c
    df['distance'] = total_miles

    return df


def parallelize_dataframe(df, funcao, n_cores=8):
    df_split = np.array_split(df, n_cores)
    pool = Pool(n_cores)
    df = pd.concat(pool.map(funcao, df_split))
    pool.close()
    pool.join()

    return df


arquivo = 'TESTES/Bases/new_york_hotels.csv'
base = pd.read_csv(
    arquivo,
    encoding='ISO-8859-1'
)

inicio = time.time()

# df_distancia = haversine(base)
df_distancia = parallelize_dataframe(base, haversine)

fim = time.time()

print(f'Tempo de execução: {(fim - inicio) * 1000}')
