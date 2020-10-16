# 68. Zip e Zip_longest - Unindo iteráveis

from itertools import zip_longest, count

indice = count()
cidades = [
    "Rio de Janeiro",
    "Curitiba",
    "São Paulo",
    "Florianópolis",
    "Porto Alegre",
]
estados = ["RJ", "PR", "SP", "SC"]

cidades_estados = zip(estados, cidades)
print(list(cidades_estados))
print(type(list(cidades_estados)))

cidades_estados = zip(indice, estados, cidades,)

for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)
