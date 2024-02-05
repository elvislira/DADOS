import pandas as pd

base = {
    'Nomes': ['Ana', 'Carlos', 'Gabriela', 'Maria'],
    'Telefones': [976846513, 861524875, 915234106, 935130673]
}

agenda = pd.DataFrame(base)

print(agenda)
