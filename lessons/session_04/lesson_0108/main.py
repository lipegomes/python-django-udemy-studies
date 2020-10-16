# 108. Métodos mágicos - Python Orientado a Objetos

"""
https://rszalski.github.io/magicmethods/
"""


class A:  # em python todas as classes derivam de object
    def __new__(cls, *args, **kwargs):
        cls.nome = input("Digite um nome: ")
        cls.idade = input("Digite a sua idade: ")

        def frase(*args, **kwargs):
            print(
                f"{cls.nome} é inteligente, "
                f"{cls.nome} têm '{cls.idade}' anos de idade."
            )

        cls.frase = frase

        # return super().__new__(cls)
        return object.__new__(cls)

    def __init__(self):  # inicializador da class em python
        print("Eu sou o INIT")


a1 = A()
print(type(a1))
print(a1.nome)
print(a1.idade)
a1.frase()

print()


class B:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_jaexiste"):
            cls._jaexiste = object.__new__(cls)

        return cls._jaexiste

    def __init__(self):
        print("Eu sou o INIT")


b1 = B()
b2 = B()
b3 = B()

print(b1 == b2)
print(b1 != b3)

print(id(b1), id(b2), id(b3))

print()


class C:
    def __init__(self):
        # print('Metodo __call__')
        pass

    def __call__(self, *args, **kwargs):
        # print(args)
        # print(kwargs)
        resultado = 1

        for i in args:
            resultado *= i
        return resultado


c1 = C()
# c1(1, 2, 3, 4, 5, nome='Bob')
variavel = c1(12, 27, 54, 36, 28)
print(variavel)

print()


class D:
    def __init__(self):
        pass

    def __setattr__(self, name, value):
        # return super().__setattr__(name, value)
        self.__dict__[name] = value


d1 = D()
d1.name = "Python Snake"
print(d1.name)

print()


class E:
    def __init__(self):
        pass

    def __del__(self):
        print("Objeto coletado.")


e = E()

print()


class F:
    def __init__(self):
        pass

    def __str__(self):
        return "<class 'A'>"


f = F()
print(f)


class G:
    def __init__(self):
        pass

    def __len__(self):
        return int(input("Digite um número: "))


g = G()
print(len(g))
