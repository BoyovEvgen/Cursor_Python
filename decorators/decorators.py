import logging
date_strftime_format = "%d-%b-%y %H:%M:%S"
message_format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='main.log', format=message_format,
                    datefmt=date_strftime_format, encoding='UTF-8', level=logging.INFO)
# 1. double_result
# This decorator function should return the result of another function multiplied by two


def double_result(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return wrapper


def add(a, b):
    return a + b


print(add(5, 5))  # 10


@double_result
def add(a, b):
    return a + b


print(add(5, 5))  # 20

#
# # 2. only_odd_parameters
# # This decorator function should only allow a function to have odd numbers as parameters,
# # otherwise, return the string "Please use only odd numbers!"


def only_odd_parameters(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg % 2 == 0:
                return "Please use only odd numbers!"
        return func(*args, **kwargs)
    return wrapper


@only_odd_parameters
def add(a, b):
    return a + b


print(add(5, 5))  # 10
print(add(4, 4))  # "Please use only odd numbers!"


@only_odd_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e


print(multiply(1, 2, 3, 4, 5))
print(multiply(9, 1, 5, 3, 7))


# # 3.* logged
# # Write a decorator which wraps functions to log function arguments and the return value on each call.
# # Provide support for both positional and named arguments (your wrapper function should take both *args
# # and **kwargs and print them both):


class LoggerDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        res = self.func(*args, **kwargs)
        logging.info(f'the function <{self.func.__name__}> accepted the following values:{args} | {kwargs}, and return {res}')
        return res


@LoggerDecorator
def my_func(*args, **kwargs):
    return 3 + len(args)


print(my_func(4, 4, 4, a=3, b="c"))
# you called func(4, 4, 4)
# it returned 6


# # 4. type_check
# # you should be able to pass 1 argument to decorator - type.
# # decorator should check if the input to the function is correct based on type.
# # If it is wrong, it should print(f"Wrong Type: {type}"), otherwise function should be executed.

def type_check(correct_type):
    def wrapper(func):
        def inner(arg):
            message = f"Wrong Type: {type(arg)} should be printed, since non-{correct_type} passed to decorated function"
            return func(arg) if type(arg) is correct_type else message
        return inner
    return wrapper


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))  # "Wrong Type: string" should be printed, since non-int passed to decorated function


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))  # "Wrong Type: list" should be printed, since non-str passed to decorated function