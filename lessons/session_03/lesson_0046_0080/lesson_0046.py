# 46. Funções (def) em Python - Parte 1

# Ao definir uma string dentro da função, ela sempre
# será impressa ao chamar a função
def say_hello():
    print("Hello World!")


say_hello()

print("----****----")


def message(msg):
    print(msg)


# Eu posso escrever o que eu quiser aqui
message("I can write whatever I want here")

print("----****----")


def salutation(msg, name):
    print(msg, name)


salutation("Hello", "Filipe")

print("----****----")


def person(msg="Welcome to Brazil", name=input("Type your name: ")):
    print(f"{msg}, {name}")


person()

print("----****----")


def name_replace(msg="Hello", name=input("Type your name: ")):
    msg = msg.replace("e", "3")
    name = name.replace("e", "3")
    print(msg, name)


name_replace()

print("----****----")


def cong_message(msg="", name=""):
    msg = "Congratulations for your new skills"
    name = input("Type your name: ")
    print(f"{msg}, {name}!!!")


cong_message()

print("----****----")


def new_message(msg="", name=""):
    msg = "Congratulations for your new skills"
    name = input("Type your name: ")
    return f"{msg}, {name}!!!"


approved = new_message()

print(approved)
