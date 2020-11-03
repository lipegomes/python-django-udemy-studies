# 80. Módulos padrão do Python

# platform renamed as 'os'('os' means operacional system)
from sys import platform as os

# randint renamed as 'ri'('ri' means randint)
from random import randint as ri

# using platform, renamed for 'os'
print(os)
print()

# using random.randint, renamed for 'ri'.
print(ri(0, 10))
print()

# using random.randint, renamed for 'ri'.
for n in range(10):
    print(ri(0, 10))
print()
