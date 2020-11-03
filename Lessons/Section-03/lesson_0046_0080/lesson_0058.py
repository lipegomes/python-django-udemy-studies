# 58. Sets em Python (Conjuntos)

"""
* add (adiciona), update(atualiza), clear , discard
* union | (une)
* intersection & (todos os elementos presentes nos dois sets)
* difference - (elementos apenas no set da esquerda)
* symmetric_diffirence ^ (Elementos que estão nos dois sets, mas não em ambos)
"""
s1 = {1, 2, 3, 4, 5}

print(s1)
print(type(s1))

for v in s1:
    print(v)


# Adicionando elementos em um set.
s2 = set()

s2.add("Petter")
s2.add("31")
s2.add("October 20")
s2.add((1, 2, 3))

print(s2)

# Discartanto(apagando) um elemento do sets
s2.discard((1, 2, 3))

print(s2)

# Update adiciona um elemento e itera sobre ele ao adicionar ao set sem
# respeitar a ordem quando é uma string.
# Update não repete os elementos ao adicionar os elementos no set
s2.update("Data Engineer")

print(s2)

s2.update([2, 1, 0, 9, 4], (7, 5, 8, 6, 10, 3))

print(s2)

# Fazendo cast de uma lista para set, afim de remover elementos
# duplicados da lista.
l1 = [1, 1, 1, 2, 4, 5, 5, 5, 5, 7, 8, 9, "José", "José"]

print(l1)

l1 = set(l1)

print(l1)
print(type(l1))

l1 = list(l1)

print(l1)
print(type(l1))

# union (une os set)
s3 = {1, 2, 3, 4, 5, 9, 10}
s4 = {1, 2, 3, 4, 5, 6, 7}
s5 = s3 | s4

print(s5)

# intersection (todos os elementos presentes nos dois sets)
s5 = s3 & s4

print(s5)

# difference (elementos apenas no set da esquerda)
s5 = s3 - s4

print(s5)

# symmetric_diffirence ^ (Elementos que estão nos dois sets, mas não em ambos)
s5 = s3 ^ s4

print(s5)


l3 = ["Wendy", "Venna", "Flower"]
l4 = ["Wendy", "Venna", "Flower", "Flower", "Flower", "Flower", "Flower"]

# Ao realizar o cast de uma lista para um set, remove-se os elementos
# duplicados contidos ma lista e o set passa a ter elementos únicos.
if set(l3) == set(l4):
    print("L3 é igual a L4")
    print(f"L3 -> {set(l3)}")
    print(f"L4 -> {set(l4)}")
else:
    print("L3 é diferente de L4")
    print(f"L3 -> {set(l3)}")
    print(f"L4 -> {set(l4)}")
