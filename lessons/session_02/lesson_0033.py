# 33. For in - Estrutura de repetição em Python

# Função range(start=0, stop, setp=1)

print("----****----")

text = "Python"
new_str = ""

for letter in text:
    if letter == "t":
        new_str += letter.upper()
    elif letter == "h":
        new_str += letter.upper()
    else:
        new_str += letter

print(f"{new_str}")

print("----****----")

for num in range(10):
    print(num)

print("----****----")

for num in range(1, 11, 1):
    print(num)

print("----****----")

for num in range(20, 9, -1):
    print(num)

print("----****----")

for num in range(100):
    if num % 29 == 0:
        print(num)

print("----****----")
