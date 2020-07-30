from data import products, persons, lis


minimum_price1 = int(input("Type a minimum price: "))
new_list3 = filter(lambda p: p["price"] >= minimum_price1, products)

for price in new_list3:
    if minimum_price1 in products:
        print(price)
    else:
        print
        (f"There is no product with this minimum value: {minimum_price1}.")
