# 104. Classes Abstratas - Python Orientado a Objetos

from abc import ABC, abstractclassmethod


class A(ABC):
    @abstractclassmethod
    def talk(self):
        pass


class B(A):
    def talk(self):
        print("Talking ... B...")


a = B()
a.talk()
