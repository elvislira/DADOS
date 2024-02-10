import pandas as pd


loja1 = {
    'Vendedor': ['Ana', 'Paulo', 'Maria', 'Miguel', 'Rafael', 'Ana'],
    'Item': ['Camisa Nike', 'Tênis Adidas', 'Camisa Nike',
             'Meias Speedo', 'Tênis Nike', 'Camisa Nike'],
    'Valor': [109.90, 299.00, 115.90, 24.99, 289.90, 99.90]
}

loja2 = {
    'Vendedor': ['Ana', 'Fernando', 'Carlos', 'Carlos', 'Carlos', 'Tânia'],
    'Item': ['Camisa Fila', 'Tênis Adidas', 'Camisa Nike',
             'Camisa Nike', 'Camisa Fila', 'Tênis Misuno'],
    'Valor': [109.90, 99.00, 115.90, 109.99, 89.90, 199.90]
}

base1 = pd.DataFrame(loja1, index=list(range(1, 7)))
base2 = pd.DataFrame(loja2, index=list(range(7, 13)))

print(f'{base1}\n')
print(f'{base2}\n')

lojas = pd.concat([
    base1,
    base2,
], axis=1)

print(f'{lojas}\n')

lojas = pd.merge(
    base1, 
    base2,
    how='inner',
    on='Item'
)

print(f'{lojas}\n')
