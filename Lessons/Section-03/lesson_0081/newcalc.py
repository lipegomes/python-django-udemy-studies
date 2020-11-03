# 81. Como criar módulos em Python

import math

PI = math.pi


def double_the_list(a):  # 'a' is argument
    return [x * 2 for x in a]


def multiply(a):  # 'a' is argument
    r = 1
    for i in a:
        r *= i
    return r


if __name__ == "__main__":
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(double_the_list(num))
    print(multiply(num))
    print(PI)
