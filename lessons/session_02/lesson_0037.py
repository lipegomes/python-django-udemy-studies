# 37. Desempacotamento de lists em Python

list1 = ["Airton Senna", "Lyffy", "Cowboy Bebop", 1, 2, 3, 4, 5]
n1, n2, n3, *new_list1, last1 = list1

print(n1, n2, new_list1, last1)

print("---------------------------------------------------------------")

list2 = ["Airton Senna", "Lyffy", "Cowboy Bebop", 1, 2, 3, 4, 5]
*new_list2, n1, n2, n3 = list2

print(new_list2, n1, n2, n3)

print("---------------------------------------------------------------")

# list3 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# n1, n2, *new_list3, n3, n4, last3 = list3

# print(n1, n2, *new_list3, n3, n4, last3)

# print("---------------------------------------------------------------")
# refazer a lista 3
