# 83. Criando, lendo, escrevendo e apagando arquivos

# Imports
import os
import json

# non-pythonic ways (Maneiras não pythinicas)
file1 = open("test1.txt", "w+")
file1.write("Line 1\n")
file1.write("Line 2\n")
file1.write("Line 3\n")

file1.seek(0, 0)
print("READ LINES:")
print(file1.read())
print("*" * 20)

file1.seek(0, 0)
print(file1.readline(), end="")
print(file1.readline(), end="")
print(file1.readline(), end="")
print("*" * 20)

file1.seek(0, 0)
for line in file1.readlines():
    print(line, end="")
print("*" * 20)

file1.seek(0, 0)
for line in file1:
    print(line, end="")

print("*" * 20)

file1.close()


try:
    file2 = open("test2.txt", "w+")
    file2.write("Line")
    print(file2.read())
finally:
    file2.close()


# Write in Pythonic way (Escrevendo de forma Pythonica)
with open("test3.txt", "w+") as file3:
    file3.write("Line 1\n")
    file3.write("Line 2\n")
    file3.write("Line 3\n")

    file3.seek(0)
    print(file3.read())

# Read in Pythonic way (Leitura)
with open("test3.txt", "r+") as file3:
    print(file3.read())

# Append mode in Pythonic way (Adicionando ao final)
with open("test3.txt", "a+") as file3:
    file3.write("Another line")
    file3.seek(0)
    print(file3.read())


# Remove archives
os.remove("test1.txt")


# Json
d1 = {
    "Person 1": {"name": "Filipe", "age": "29"},
    "Person 2": {"name": "Aleksandra", "age": "31"},
}

d1_json = json.dumps(d1, indent=True)

with open("persons.json", "w+") as file:
    file.write(d1_json)
