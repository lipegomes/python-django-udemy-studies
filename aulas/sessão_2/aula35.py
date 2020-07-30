# 35. FOR / ELSE em Python

names1 = ["Cowboy Bebop", "Ayrton Senna", "Luffy"]

for valor in names1:
    if valor.startswith("A"):
        print("Starts with 'A':", valor)
    else:
        print("Doesn't start with 'A':", valor)

print("----****----")

names2 = ["Cowboy Bebop", "Ayrton Senna", "Luffy"]
start_whith_a = False
for valor in names2:
    if valor.startswith("A"):
        start_whith_a = True

if start_whith_a:
    print(f"There is a word that starts with 'A'.")
else:
    print("There is no word that starts with 'A'.")
