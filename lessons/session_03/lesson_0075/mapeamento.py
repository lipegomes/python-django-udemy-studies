from data import products, persons, lis

new_list1 = list(map(lambda x: x * 2, lis))
print(new_list1)
print()

new_list2 = list([x * 2 for x in lis])
print(new_list2)
print()


def increase_price(p):
    p["price"] = round(p["price"] * 1.05, 2)
    return p


new_products = map(increase_price, products)

for product in new_products:
    print(product)


names = map(lambda p: p["name"], persons)

for people in names:
    print(people)


def increasing_age(a):
    a["new_age"] = round(a["age"] * 1.20)
    return a


names = map(increasing_age, persons)

for persons in names:
    print(persons)
