from data import products, persons, lis


# filter
new_list1 = filter(lambda x: x > 5, lis)
print(list(new_list1))
print(type(new_list1))
print()

# list comprehension
new_list2 = [x for x in lis if x > 5]
print(new_list2)
print(type(new_list2))
print()

# filter
minimum_price1 = int(input("Type a minimum price: "))
new_list3 = filter(lambda p: p["price"] >= minimum_price1, products)

for price in new_list3:
    # if minimum_price1 not in products:
    #     print(f'There is no product with this value: {minimum_price1}.')
    # else:
    #     break
    print(price)
print()


def price_filtration(product):
    if product["price"] > 50:
        product["expensive"] = True
    return True


new_list4 = filter(price_filtration, products)

for price in new_list4:
    print(price)
print()


def person_filtration(person):
    if person["age"] < 18:
        person["old"] = True
    return True


new_list5 = filter(person_filtration, persons)

for person in new_list5:
    print(person)
print()
