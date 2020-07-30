# 76. Reduce

from data import products, persons, lis
from functools import reduce


# ac: acumulador , i: item
print()

soma_lista = reduce(lambda ac, i: i + ac, lis, 0)
print(soma_lista)
print()


soma_precos = reduce(lambda ac, p: p["price"] + ac, products, 0)
print(f"Soma dos preços R${soma_precos}")
print(f"Média dos preços R${soma_precos / len(products)}")
print()
