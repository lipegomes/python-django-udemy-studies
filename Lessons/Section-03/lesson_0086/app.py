# 86. Problema dos parâmetros mutáveis em funções


def lista_de_clientes(clientes_interavel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_interavel)
    return lista


clientes1 = lista_de_clientes(["João", "Maria", "Eduardo"])

clientes2 = lista_de_clientes(["Marcos", "Jonas", "Zico"])

print(clientes1)
print(clientes2)
