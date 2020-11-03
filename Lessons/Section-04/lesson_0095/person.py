# 95. Métodos estáticos - Python Orientado a Objetos

from datetime import datetime
from random import randint


class Person:
    current_year = int(datetime.strftime(datetime.now(), "%Y"))

    def __init__(self, name, age):  # (instance, parameter, parameter)
        self.name = name
        self.age = age

    def get_birth_year(self):  # instance method
        print(self.current_year - self.age)

    @classmethod
    def person_birth_year(cls, name, birth_year):  # (class,parameter, parameter)
        age = cls.current_year - birth_year
        return cls(name, age)

    @staticmethod
    def generate_id():
        rand1 = randint(10000, 19999)
        rand2 = randint(1, 10)
        return f"{Person.current_year}-SPE-{rand1}-{rand2}"


# p1 = Person.person_birth_year('Beatrice', 1940)
# p1 = Person("George", 75)
# print(p1)
# print(p1.name, p1.age)
# p1.get_birth_year()
# print(p1.generate_id())
