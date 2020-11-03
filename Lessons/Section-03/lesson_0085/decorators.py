# 85. Funções decoradoras e decoradores
from time import time, sleep


def master(function1):
    def senior(*args, **kwargs):
        print("___*___The function is decorated___*___\n")
        function1(*args, **kwargs)

    return senior


@master  # decorate
def say_something(msg=""):
    say = input("Type a phrase: ")
    print(say)


@master
def say_hi(msg=""):
    name = input("Type your name: ")
    print(f"Hello {name} !!!")


# say_something = master(say_something) -> docorate
say_something()
say_hi()


# This function calculates the speed of a function.


def speed(function2):
    def internal(*args, **kwargs):
        start_time = time()
        result = function2(*args, **kwargs)
        end_time = time()
        total_time = (end_time - start_time) * 1000
        print(
            f"\nThe function {function2.__name__} "
            f"it took {total_time:.2f}ms to run."
        )
        return result

    return internal


@speed
def delay():
    for i in range(100):
        print(i, end="")
        # sleep(1)


delay()
