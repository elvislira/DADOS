import pandas as pd


dados = {
    'Vendedor': ['Ana', 'Paulo', 'Maria', 'Miguel', 'Rafael', 'Ana'],
    'Item': ['Camisa Nike', 'Tênis Adidas', 'Camisa Nike',
             'Meias Speedo', 'Tênis Nike', 'Camisa Nike'],
    'Valor': [109.90, 299.00, 115.90, 24.99, 289.90, 99.90]
}

base = pd.DataFrame(dados)

print(f'{base}\n')

itens = base.groupby('Item')

print(itens.count())

print(itens.describe())

vendedores = base.groupby('Vendedor')

print(vendedores.sum())