# 56. Dicionários em Python

import copy

d1 = {"chave1": "valor da chave"}
d1["nova chave"] = "valor da nova chave"

print(d1)
print("-*-" * 20)


# As keys(chaves) dentro dos dicionarios precisam ser unicas
# cada chave tem que ter o seu próprio valor
d2 = dict(key1="valor1", key2="valor2")
d2["key3"] = "valor3"

print(d2)
print("-*-" * 20)


d3 = {
    "str": "valor",
    123: "outro valor",
    (1, 2, 3, 4): "Tupla",
}

print(d3)
print(d3[(1, 2, 3, 4)])
print(type(d3[(1, 2, 3, 4)]))

d3["naoexiste"] = "Agora existe."
if "naoexiste" not in d3:
    print(d3["naoexiste"])

print("OI")
print("-*-" * 20)


d4 = {
    "Monkey D.Luffy": 19,
    "Roronoa Zoro": 21,
    "Vinsmoke Sanji": 21,
    "Brook": 90,
    "Franky": 36,
    "Tony Tony Chopper": 17,
    "Usopp": 19,
    "Nami": 20,
    "Nico Robin": 30,
}

if d4.get("keyname") is not None:
    print(d4.get("keyname"))

print("NOT IS METTER")

d4["Monkey D.Luffy"] = "21"
if d4.get("Monkey D.Luffy") is not None:
    print(d4.get("Monkey D.Luffy"))

print(d4)

d4.update({"Bob Jeff": 50})

print(d4)

print("John Jonnes" in d4)
print("John Jonnes" in d4.keys())
print(29 in d4.values())

print(len(d4))
print("-*-" * 20)

for k, v in d4.items():
    print(k, v)
print("-*-" * 20)

clientes = {
    "cliente1": {"nome": "King", "sobrenome": "Arthur},
    "cliente2": {"nome": "Lord", "sobrenome": "Dark"},
}

for clientes_k, clientes_v in clientes.items():
    print(f"Exibindo {clientes_k}")
    for dados_k, dados_v in clientes_v.items():
        print(f"\t{dados_k}, {dados_v}")
print("-*-" * 20)


d5 = {1: "a", 2: "b", 3: "c", "d": ["London", "Bridge"]}
v = copy.deepcopy(d5)
v[1] = "Marry"

print(v["d"][0])

print(d5)
print(v)
print("-*-" * 20)

# Convertendo uma lista em dicionário
lista1 = [
    ["c1", 1],
    ["c2", 2],
    ["c3", 3],
]

d6 = dict(lista1)
print(d6)
print(type(d6))
print("-*-" * 20)

# Convertendo uma tupla em dicionário
lista2 = (
    ["c1", 1],
    ["c2", 2],
    ["c3", 3],
)

d7 = dict(lista2)
print(d7)
print(type(d7))
print("-*-" * 20)


d8 = {
    1: 2,
    2: 3,
    3: 4,
    4: 5,
}

d8.pop(4)
print(d8)

d8.popitem()
print(d8)

# Concatenando dicionários
d9 = {
    "a": "b",
    "b": "c",
}

d8.update(d9)
print(d8)
