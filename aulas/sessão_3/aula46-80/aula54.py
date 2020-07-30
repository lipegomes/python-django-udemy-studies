# 54. Expressões lambda (funções anônimas) em Python

list1 = [
    ["P1", 10],
    ["P2", 16],
    ["P3", 27],
    ["P4", 14],
    ["P5", 32],
]

list1.sort(key=lambda item: item[1], reverse=True)
print(list1)


list2 = [
    ["P1", 120],
    ["P2", 11244],
    ["P3", 217],
    ["P4", 28975],
    ["P5", 100],
]

# Ordenando pelo nome do produto
print(sorted(list2, key=lambda i: i[0], reverse=False))
# Ordenando pelo maior valor do produdo
print(sorted(list2, key=lambda i: i[1], reverse=True))


list3 = [
    ["Monkey D.Luffy", 19],
    ["Roronoa Zoro", 21],
    ["Vinsmoke Sanji", 21],
    ["Brook", 90],
    ["Franky", 36],
    ["Tony Tony Chopper", 17],
    ["Usopp", 19],
    ["Nami", 20],
    ["Nico Robin", 30],
]

print(sorted(list3, key=lambda n: n[0], reverse=False))
print(sorted(list3, key=lambda i: i[1], reverse=True))
