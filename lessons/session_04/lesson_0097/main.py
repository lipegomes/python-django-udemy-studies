# 97. Atributos de Classe - Python Orientado a Objetos


class A:
    vc = 123

    def __init__(self):
        self.vc = 321


a1 = A()
a2 = A()
a3 = A.vc

print(a1.__dict__)
print(a2.__dict__)
print(A.__dict__)

print(a1.vc)
print(a2.vc)
print(a3)
