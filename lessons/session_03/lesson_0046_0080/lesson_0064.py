# 64. Geradores, Iteradores e Iteráveis em Python
import sys
import time


l1 = [0, 1, 2, 3, 4, 5]
# Verificando se l1 é iterável
print(hasattr(l1, "__iter__"))
# verificando se a lista é um iterador
print(hasattr(l1, "__next__"))
print()

# for transforma a lista em um itarador e utiliza
# o iterador para exibir o valor em cada linha.
for v in l1:
    print(v)
print()


# def gera1():
#     r = []
#     for n in range(100):
#         r.append(n)
#         time.sleep(0.1)
#     return r


# g1 = gera1()

# for v in g1:
#     print(v)


def gera2():
    for n in range(100):
        yield n
        time.sleep(0)


g2 = gera2()

for v in g2:
    print(v)


l2 = [x for x in range(100)]
print(type(l2))
print(sys.getsizeof(l2))

l3 = (x for x in range(100))
print(type(l3))
print(sys.getsizeof(l3))
