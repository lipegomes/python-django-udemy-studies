# 31. While/Else - Repetição com accumulatores em Python

counter = 1
accumulator = 1

print("c", "a")

while counter <= 100:

    print(counter, accumulator)

    accumulator += counter
    counter += 1

    if counter > 100:
        break

else:
    print("End !!!")
