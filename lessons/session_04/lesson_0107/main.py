# 107. Sobrecarga de operadores - Python Orientado a Objetos

"""
No Python, o comportamento de operadores é definido por métodos especiais.
Vamos alterar o comportamento de operadores com classes definidas pelo usuário.
"""


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y

    def __repr__(self):
        return f"<class 'Rectangle({self.x}, {self.y})'>"

    def __add__(self, other):  # sobrecarga de operador
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Rectangle(new_x, new_y)

    def __lt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
        else:
            return False

    def __gt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 > a2:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)
r3 = r1 + r2

print(r3 == r2)
