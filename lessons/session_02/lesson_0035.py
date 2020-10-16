# 35. FOR / ELSE em Python

names1 = [
    "Cowboy Bebop",
    "Ayrton Senna",
    "Luffy",
    "Marry",
    "Wendy",
    "Louis",
    "Kate",
    "Kiara",
    "Luanny",
    "Mark",
    "Petter",
    "Barbara",
]

for valor in names1:
    if valor.startswith("A"):
        print("Starts with 'A':", valor)
    else:
        print("Doesn't start with 'A':", valor)

print("----****----")

names2 = ["Lindinha", "Duque", "Floquinho"]
start_whith_a = False
for valor in names2:
    if valor.startswith("A"):
        start_whith_a = True

if start_whith_a:
    print("There is a name that starts with 'A'.")
else:
    print("There is no name that starts with 'A'.")
