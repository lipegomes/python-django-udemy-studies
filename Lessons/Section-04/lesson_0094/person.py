from datetime import datetime


class Person:
    current_year = int(datetime.strftime(datetime.now(), "%Y"))

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_birth_year(self):
        print(self.current_year - self.age)

    @classmethod
    def person_birth_year(cls, name, birth_year):
        age = cls.current_year - birth_year
        return cls(name, age)


# p1 = Person.person_birth_year('Kira', 1800)
# p1 = Person("Cowboy Bebbop", 32)
# print(p1)
# print(p1.name, p1.age)
# p1.get_birth_year()
