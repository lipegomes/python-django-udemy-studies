from person import Person

p1 = Person("George", 75)

# print class and object
print(p1)

print(p1.name, p1.age)

p1.get_birth_year()

print(p1.generate_id())

p2 = Person("Beatrice", 80)

print(
    f"{p2.name} is {p2.age} years old, was born in {Person.current_year - p2.age}. "
    f"Your id is {p2.generate_id()}."
)
