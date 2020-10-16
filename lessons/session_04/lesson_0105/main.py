# 105. Polimorfismo de sobreposição - Python Orientado a Objetos

"""
Polimorfismo é o principio que permite que classes derivadas de uma mesma
superclasse tenham métodods iguais ( de mesma assinatura) mas comportamentos
diferentes.
Mesma assinatura = Mesma quantidade e topo de parâmetros
"""
from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def speak(self, msg):
        pass


class B(A):  # classe B herda a classe A
    def speak(self, msg):
        print(f'B talking "{msg}"')


class C(A):  # classe B herda a classe A
    def speak(self, msg):
        print(f'C talking "{msg}"')


b = B()
c = C()

b.speak("The day is beautifull")
c.speak("The beach ins great and the sum in blue")
