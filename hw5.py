# 1.
class Laptop:
    """
    Make the class with composition.
    """

    def __init__(self):
        self.battery = Battery()


class Battery:
    """
    Make the class with composition.
    """

    def __init__(self):
        self.power = 1000
        self.battery_type = 'lithium-polimer'


# 2.
class Guitar:
    """
    Make the class with aggregation
    """

    def __init__(self):
        self.lst_string = []

    def set_string(self, strings: list):
        for i in range(6):
            self.lst_string.append(strings[i])
            print(f'{strings[i]} mounted on guitar')


class GuitarString:
    """
    Make the class with aggregation
    """
    num_string = 0

    def __new__(cls, *args, **kwargs):
        cls.num_string += 1
        return super(GuitarString, cls).__new__(cls)

    def __init__(self):
        self.name_str = GuitarString.num_string
        print(f'{self} created')

    def __repr__(self):
        return f"Object: string nomber {self.name_str}"


lst_string = [GuitarString() for _ in range(7)]
my_guitar = Guitar()
my_guitar.set_string(lst_string)


# # 3
class Calc:
    """
    Створіть клас з одним методом "add_nums" та 3 атрибутами, який повертає суму цих атрибутів.
    """

    def __init__(self, first: int, second: int, third: int):
        self.first = first
        self.second = second
        self.third = third

    def add_nums(self):
        return self.first + self.second + self.third


# 4*.
class Pasta:
    """
    Створіть клас, який приймає 1 атрибут при ініціалізації - ingredients і визначає інгридієнти атрибута екземпляра.
    Він повинен мати 2 методи:
    carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
    which should create Pasta instances with predefined list of ingredients.
    который должен создавать экземпляры Pasta с предопределенным списком ингредиентов.
    Example:
        pasta_1 = Pasta(["tomato", "cucumber"])
        pasta_1.ingredients will equal to ["tomato", "cucumber"]
        pasta_2 = Pasta.bolognaise()
        pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
    """

    def __init__(self, ingredients):
        self.ingradients = ingredients
        if 'forcemeat' and 'tomatoes' in ingredients:
            self.name = 'carbonara'
        elif 'bacon' and 'parmesan' and 'eggs' in ingredients:
            self.name = 'bolognaise'
        else:
            self.name = 'unknown pasta'

    @classmethod
    def carbonara(cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])


pasta_1 = Pasta.carbonara()
print(f'Pasta_1: {pasta_1.name},  ingredients will equal to {pasta_1.ingradients}')
pasta_2 = Pasta.bolognaise()
print(f'Pasta_2: {pasta_2.name},  ingredients will equal to {pasta_2.ingradients}')
pasta_3 = Pasta(['forcemeat', 'tomatoes'])
print(f'Pasta_3: {pasta_3.name},  ingredients will equal to {pasta_3.ingradients}')


# 5*.
class Concert:
    """
    Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
    Example:
        Concert.max_visitor_num = 50
        concert = Concert()
        concert.visitors_count = 1000
        print(concert.visitors_count)  # 50
    """
    max_visitor_num = 0

    def __init__(self):
        self._visitors_count = 0

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        self._visitors_count = value if value <= Concert.max_visitor_num else Concert.max_visitor_num


Concert.max_visitor_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)

# 6.
"""
Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
"""
import dataclasses


@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


my_object = AddressBookDataClass(1, 'Evgen', '06896456544', 'USA', 'qwe@qwe.qwe', '01.01.2000', 23)
print(my_object.name, my_object.birthday)


# 7. Create the same class (6) but using NamedTuple

import collections

AddressBookDataClass_2 = collections.namedtuple('AddressBookDataClass', ['key', 'name', 'phone_number', 'address',
                                                                       'email', 'birthday', 'age'])
my_object_2 = AddressBookDataClass_2(1, 'Evgen', '06896456544', 'USA', 'qwe@qwe.qwe', '01.01.2000', 23)
print(my_object_2.name, my_object_2.birthday)

# 8.


class AddressBook:
    """
    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
    Expected result by printing instance of AddressBook: AddressBook(key='', name='', phone_number='', address='', email='', birthday= '', age='')
    """
    def __init__(self, key: int, name: str, phone_number: str, address: str, email: str, birthday: str, age: int):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __repr__(self):
        return f'AddressBook(key= {self.key}, name= {self.name}, phone_number= {self.phone_number},' \
               f'address= {self.address}, email= {self.email}, birthday= {self.birthday}, age= {self.age})'


my_object_3 = AddressBook(1, 'Evgen', '06896456544', 'USA', 'qwe@qwe.qwe', '01.01.2000', 23)
print(my_object_3)


# 9. !!!!!!!!Не зовсім зрозумів завдання, можливо потрібно виконати шось з цього...
class Person:
    """
    Change the value of the age property of the person object
    """
    name = "John"
    age = 36
    country = "USA"

    # @property
    # def age(self):
    #     return self.age
    #
    # @age.setter
    # def age(self, new_age):
    #     self.age = new_age


my_person = Person
my_person.age = 30
print(my_person.age)
my_person_2 = Person
print(my_person_2.age)


# 10.


class Student:
    """
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    Добавьте атрибут 'email' объекта student и задайте его значение
# Назначьте новый атрибут переменной 'student_email' и распечатайте его с помощью getattr
    """
    id = 0
    name = ""

    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.student_email = email


student = Student(1, 'Evgen', 'qwe@qwe.qwe')
email = getattr(student, 'student_email')
print(email)
