# 96. @property - Getters e Setters - Python Orientado a Objetos

from products import Products


p1 = Products("Hardcover notebook", 20)
p1.discount(10)

print(f"Item: {p1.item}",f"\nPrice: ${round(p1.price, 2)}")

p2 = Products("@Python for beginners", "$19.59")
p2.discount(10)

print(f"Item: {p2.item}",f"\nPrice: ${round(p2.price, 2)}")
