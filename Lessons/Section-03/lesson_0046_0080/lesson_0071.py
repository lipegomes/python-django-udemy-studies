# 71. Count - Contadores infinitos

from itertools import count

contador = count(start=5, step=0.1)

for valor in contador:
    print(round(valor, 2))

    if valor >= 10:
        break
