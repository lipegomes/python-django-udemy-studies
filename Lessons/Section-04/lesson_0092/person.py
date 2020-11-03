from datetime import datetime


class Person:
    current_year = int(datetime.strftime(datetime.now(), "%Y"))

    def __init__(self, name, age, eating=False, speaking=False):
        self.name = name
        self.age = age
        self.eating = eating
        self.speaking = speaking

    def speak(self, subject):
        if self.eating:
            print(f"{self.name} can't talk eating.")
            return

        if self.speaking:
            print(f"{self.name} is already talking.")
            return

        print(f"{self.name} is talking.")
        self.speaking = True

    def stop_speak(self):
        if not self.speak:
            print(f"{self.name} can't talking.")
            return

        print(f"{self.name} stop talking.")
        self.speaking = False

    def eat(self, food=""):
        food = input("Type a food: ")

        if self.eating:
            print(f"{self.name} is already eating.")
            return

        if self.speaking:
            print(f"{self.name} can't eat talking.")

        print(f"{self.name} is eating {food}.")
        self.eating = True

    def stop_eat(self):
        if not self.eating:
            print(f"{self.name} is not eating.")
            return

        print(f"{self.name} stop eating.")
        self.eating = False

    def get_birth_year(self):
        return self.current_year - self.age
