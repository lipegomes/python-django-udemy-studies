# 55. Tuplas em Python

t1 = (1, 2, 3, "a", "b", "c")

print(type(t1))
print(t1)
print(t1[3])

for v in t1:
    print(v)

print(t1[-3:])


t2 = 10, 20, 30

print(type(t2))
print(t2)


t3 = 1, 2, 3, 4, 5
t4 = 6, 7, 8, 0, 10
t5 = t3 + t4

n1, n2, n3, *_ = t5

print(t5)


t6 = ("-*-") * 20

print(t6)


t7 = (1, 2, 3, 4, 5)
t7 = list(t7)

t7.append(6)
print(t7)

t7[5] = True
print(t7)

t7 = tuple(t7)

print(t7)
print(type(t7))
