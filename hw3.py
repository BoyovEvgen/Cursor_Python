# 1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print(f'id "int_a" - {id(int_a)}\n'
      f'id "str_b" - {id(str_b)}\n'
      f'id "set_c" - {id(set_c)}\n'
      f'id "lst_d" - {id(lst_d)}\n'
      f'id "dict_e" - {id(dict_e)}\n')

# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print(f'id "lst_d" after the change: {id(lst_d)}')

# 3. Define the type of each object from step 1.
print(f'Type of "int_a": {type(int_a)}\n'
      f'Type of "str_b": {type(str_b)}\n'
      f'Type of "set_c": {type(set_c)}\n'
      f'Type of "lst_d": {type(lst_d)}\n'
      f'Type of "dict_e": {type(dict_e)}\n')

# 4*. Check the type of the objects by using isinstance.
print(f'Type variable "int_a" is int, {isinstance(int_a, int)}\n'
      f'Type variable "str_b" is str , {isinstance(str_b, str)}\n'
      f'Type variable "set_c" is set, {isinstance(set_c, set)}\n'
      f'Type variable "lst_d" is list, {isinstance(lst_d, list)}\n'
      f'Type variable "dict_e" is dict, {isinstance(dict_e, dict)}\n')

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."
#
# 5. With .format and curly braces {}
print('Anna has {} apples and {} peaches.'.format(5, 3))

# 6. By passing index numbers into the curly braces.
print('Anna has {1} apples and {0} peaches.'.format(5, 3))

# 7. By using keyword arguments into the curly braces.
print('Anna has {a} apples and {p} peaches.'.format(a=5, p=3))

# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print('Anna has {a} apples and {p} peaches.'.format(a=5*'@', p=3*'@'))

# 9. With f-strings and variables
a = 5
p = 3
print(f'Anna has {a} apples and {p} peaches.')

# 10. With % operator
print('Anna has %d apples and %d peaches.' % (3, 5))

# 11*. With variable substitutions by name (hint: by using dict)
print('Anna has %(a)d apples and %(p)d peaches.' % {'a': 5, 'p': 3})

# Comprehensions:
# (1)
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)

# (2)
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]

# 12. Convert (1) to list comprehension
lst1 = [num**2 if num % 2 ==1 else num**4 for num in range(10)]
print(lst1)

# 13. Convert (2) to regular for with if-else

lst2 = []
for num in range(10):
    if num % 2 == 0:
        lst2.append(num // 2)
    else:
        lst2.append(num * 10)
print(lst2)
print(list_comprehension)

# (3)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)

# 14. Convert (3) to dict comprehension.
d_comprehension = {num: num**2 for num in range(1, 11) if num % 2 == 1}
print(d_comprehension)

# (4)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)
# 15*. Convert (4) to dict comprehension.
d_comprehension = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(d_comprehension)

# (5)
dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(dict_comprehension)
# 16. Convert (5) to regular for with if.
dict_comprehension = {}
for x in range(10):
    if x**3 % 4 == 0:
        dict_comprehension[x] = x**3
print(dict_comprehension)

# (6)
dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
print(dict_comprehension)
# 17*. Convert (6) to regular for with if-else.
dict_comprehension = {}
for x in range(10):
    if x**3 % 4 == 0:
        dict_comprehension[x] = x**3
    else:
        dict_comprehension[x] = x
print(dict_comprehension)

# Lambda:

# (7)


def foo(x, y):
    if x < y:
        return x
    else:
        return y

# 18. Convert (7) to lambda function


res = lambda x, y: x if x < y else y
print(foo(5, 4))
print(res(5, 4))

# (8)
foo2 = lambda x, y, z: z if y < x and x > z else y


# 19*. Convert (8) to regular function


def foo3(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y


print(foo2(1, 2, 3))
print(foo3(1, 2, 3))


lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
# 20. Sort lst_to_sort from min tomax
lst_to_sort.sort()
print(lst_to_sort)

# 21. Sort lst_to_sort from max to min
lst_to_sort.sort(reverse=True)
print(lst_to_sort)

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
print(list(map(lambda x: x*2, lst_to_sort)))


# 23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_new = list(map(lambda x, y: x + y, list_A, list_B))
print(list_new)

# 24. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_24 = list(filter(lambda x: x % 2 == 1, lst_to_sort))
print(lst_24)


# 25. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
b = range(-10, 10)
print(list(filter(lambda x: x > 0, b)))

# 26*. Using the filter function, find the values that are common to the two lists:
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
set_1 = set(list_1)
set_2 = set(list_2)
print(set_1.intersection(set_2))