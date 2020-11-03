# 60. List Comprehension em Python

l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ex1 = [v for v in l1]

print(ex1)

ex2 = [v * 2 for v in l1]
ex3 = [(v1, v2) for v1 in l1 for v2 in range(3)]

print(ex2)
print(ex3)

l2 = ["Cowboy", "Bebop"]
ex4 = [v.replace("o", "@") for v in l2]

print(ex4)


tupla = (
    ("key1", "valor1"),
    ("key2", "valor2"),
)

ex5 = [(x, y) for x, y in tupla]
ex5 = dict(ex5)  # type cast
print(ex5)


l3 = list(range(100))
# Números que são divisíveis por 3 e por 8 com resto ZERO.
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
# Números que são divisíveis por 3.
ex7 = [v if v % 3 == 0 else "Não é" for v in l3]

print(f"Ex6: {ex6}")
print(f"Ex7: {ex7}")
