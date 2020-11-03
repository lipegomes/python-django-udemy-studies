from exchange.calc_price import increase, reduction
from exchange.moeda import real

# print(f"\n{'-*-' * 20}")


# pant_price = 60.0
# new_pant_price = increase(valor=pant_price, percentage=8, conversion=True)
# # Percentage increase in the price of each pant
# perc_increase_pant = ((float(new_pant_price) - pant_price) / pant_price) * 100

# print()
# print(f"Inicial pant price: {real(pant_price)}")
# print(f"New pant price: {real(new_pant_price)}")
# print(
#     f"The price increase for each pant was: "
#     f"{real(new_pant_price - pant_price)}"
# )
# print(f"Percentage increase pant: {perc_increase_pant}%")


# print(f"\n{'-*-' * 20}")


# shirt_price = 40
# new_shirt_price = reduction(valor=shirt_price, percentage=25, conversion=True)
# # Percentage reduction in the price of each shirt
# perc_reduction_shirt = ((new_shirt_price - shirt_price) / shirt_price) * 100

# print()
# print(f"Inicial shirt price: {real(shirt_price)}")
# print(f"New shirt price: {real(new_shirt_price)}")
# print(
#     f"The price reduction for each shirt was: "
#     f"${real(new_shirt_price - shirt_price)}"
# )
# print(f"Percentage reduction shirt: {perc_reduction_shirt}%")
# print(f"\n{'-*-' * 20}")

price1 = 49.99
price_increase1 = increase(valor=price1, percentage=20, conversion=True)
print(f"\n{real(price_increase1)}")

price2 = 49.99
price_reduction2 = reduction(valor=price2, percentage=20, conversion=True)
print(f"{real(price_reduction2)}")
print(f"\n{'-*-' * 20}")
