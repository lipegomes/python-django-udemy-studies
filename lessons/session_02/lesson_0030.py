# 30. While - Estrutura de repetição em Python

from itertools import product

print("---------------------------------------------------")

male_anime_char = ["Akira", "Goku", "Luffy", "Gajeel", "Ken", "Masaru"]
female_anime_char = ["Emiko", "Hana", "Harumi", "Kaori", "Mayu", "Naomi"]

while True:
    print(f"\n{male_anime_char}")
    print(f"\n{female_anime_char}")

    char = input("\nEnter a name from the lists: ")

    for male, female in product(male_anime_char, female_anime_char):
        if char in male:
            print(f"\nThe character {char} is male.")
            break
        elif char in female:
            print(f"\nThe character {char} is female.")
            break
    else:
        if male != male_anime_char:
            print(f"\nThe name {char},is not contained in the lists.")
            break
        elif female != male_anime_char:
            print(f"\nThe name {char},is not contained in the lists.")
            break

print("---------------------------------------------------")
pass

x = 0

while x < 10:
    if x == 10:
        x += 1
        break

    print(x)
    x += 1
print("End")
pass

print("---------------------------------------------------")

while True:
    num1 = float(input("Enter a number: "))  # type cast
    num2 = float(input("Enter another number: "))  # type cast
    operator = input("Enter a numeric operator: ")

    # Operators + - / *
    if operator == "+":
        print(f"The sum between {num1} and {num2} is {num1 + num2}.")
    elif operator == "-":
        print(f"The subtraction between {num1} and {num2} is {num1 - num2}.")
    elif operator == "/":
        print(f"The division between {num1} and {num2} is {num1 / num2}.")
    elif operator == "*":
        print(
            f"The multiplication between {num1} and {num2} is {num1 * num2}.")
    else:
        print(
            f"The operator '{operator}' entered is invalid."
            f" Enter any of + - / * operators ."
        )
        continue
    break

print("---------------------------------------------------")
