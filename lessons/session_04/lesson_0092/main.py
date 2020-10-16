# 92. Classes - Python Orientado a Objetos

from person import Person

p1 = Person("Petter", 27)
p2 = Person("Anna", 25)

print(p1.get_birth_year())
print(p2.get_birth_year())

p3 = Person("Luffy", 19)

print(f"{p3.name} was born in {p3.get_birth_year()}, is {p3.age} years old")
print(type(p3))
