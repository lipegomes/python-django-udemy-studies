# 77. Try, Except - Tratando Exceções em Python

try:
    a = 0
    try:
        a = 10 / 5
    except:
        print("Error")
except NameError as error:
    print("Developer error, contact them")
except (IndexError, KeyError) as error:
    print("Index or Key error")
except Exception as error:
    print("An unexpected error has occurred")
else:
    print("Your code was sucessfully executeds")
    print(a)
finally:
    a = ""

print(a)

print("Let's program !!!")
