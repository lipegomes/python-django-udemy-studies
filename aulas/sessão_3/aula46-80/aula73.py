# 73. Groupby - Agrupando valores
from itertools import groupby, tee

students = [
    {"name": "Filipe", "grade": "A"},
    {"name": "Petter", "grade": "C"},
    {"name": "Maria", "grade": "B"},
    {"name": "Aleksandra", "grade": "A"},
    {"name": "John", "grade": "D"},
    {"name": "Jimmy", "grade": "C"},
    {"name": "Helena", "grade": "B"},
    {"name": "Mark", "grade": "D"},
    {"name": "Suzi", "grade": "C"},
    {"name": "Martha", "grade": "B"},
]


def order(item):
    return item["grade"]


students.sort(key=order)
grouped_students = groupby(students, order)

for grouping, grouped_valors in grouped_students:
    valor1, valor2 = tee(grouped_valors)

    print(f"Grouping: {grouping}")

    for student in valor1:
        print(f"\t{student}")

    amount = len(list(valor2))
    print(f"\t{amount} students took the note {grouping}")
    print()
