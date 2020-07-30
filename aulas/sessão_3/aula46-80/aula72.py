# 72. Combinations, Permutations e Product - Itertools

"""
Combinations - Ordem não importa
Permutations - Ordem importa
* Ambos não repetem valores únicos
Product - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product

persons = ["Luffy", "Zoro", "Namy", "Usopp", "Robin", "Bebop"]

for group1 in combinations(persons, 2):
    print(group1)

print()

for group2 in permutations(persons, 2):
    print(group2)

print()

for group3 in product(persons, repeat=2):
    print(group3)
