# 37. Desempacotamento de listas em Python

lista1 = ["Airton Senna", "Lyffy", "Cowboy Bebop", 1, 2, 3, 4, 5]

n1, n2, n3, *outra_lista1, ultimo = lista1

print(n1, n2, outra_lista1, ultimo)

print("----****----")

lista2 = ["Airton Senna", "Lyffy", "Cowboy Bebop", 1, 2, 3, 4, 5]

*outra_lista2, n1, n2, n3 = lista2

print(outra_lista2, n1, n2, n3)
