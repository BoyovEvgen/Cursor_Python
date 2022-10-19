"""
1. Створіть клас Vehicle з атрибутами екземпляра max_speed і mileage та методами increase_speed, break_speed, mileage_info
2. Створіть дочірній клас Bus, який успадкує всі змінні та методи класу Vehicle і матиме власний метод seating_capacity
3. Визначте, від якого класу успадковується клас Bus (перевірте issubclass)
4. Створіть екземпляр Bus під назвою school_bus і визначте, чи є school_bus об'єктом класу Vehicle/Bus
5. Створіть новий клас School з атрибутами екземпляра get_school_id і number_of_students та методами school_address, main_subject
6*. Створіть новий клас SchoolBus, який успадкує всі методи від School і Bus і матиме власний - bus_school_color
7. Поліморфізм: Створіть два класи: Bear, Wolf. Обидва вони повинні мати метод eat. Створіть два екземпляри: від Ведмідь і від Вовк,
створіть із нього кортеж і використовуючи спільну змінну, викличте метод eat.
Магічні методи:
Додатково: 8*. Створіть клас City з атрибутами екземпляра name i population, свторіть новий екземпляр цього класу, лише коли population > 1500,
інакше повертається повідомлення: "Your city is too small". Підказка: використовуєте для цього завдання магічні методи
"""

#1


class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def increase_speed(self, speed_add):
        print(f'Speed increased by {speed_add}km/h')

    def break_speed(self, speed_subtract):
        print(f'Speed reduced by {speed_subtract}km/h ')

    def mileage_info(self):
        return self.mileage

#2


class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)
        self.seating_capacity = self.seating_capacity()  #в завданні вказано шо це має бути метод. Мені здалось шо це має бути атрибутом, зробив і те і інше..

    def seating_capacity(self):
        return input("Set the capacity: ")


#3

print(issubclass(Bus, Vehicle))

#4
school_bus = Bus(300, 1000000)
print(isinstance(school_bus, Bus),
      isinstance(school_bus, Vehicle))

#5


class School:
    def __init__(self, school_id, number_of_students):
        self.get_school_id = school_id
        self.number_of_students = number_of_students

    def school_address(self):
        print('School address: unknown')

    def main_subject(self):
        print('Main subject: mathematics')


#6

class SchollBus(School, Bus):
    def __init__(self, school_id, number_of_students, max_speed, mileage):
        super().__init__(school_id = school_id, number_of_students = number_of_students)
        super().__init__(max_speed, mileage)

    def bus_scholl_color(self):
        return 'Color of Bus: Unknown'


sbus = SchollBus(123, 200, 350, 60000)
print(sbus.bus_scholl_color())


#7


class Animal:
    def __init__(self):
        self.name = 'animal'
        self.meal = 'meal'

    def eat(self):
        print(f'{self.name} eats {self.meal}')


class Bear(Animal):
    def __init__(self):
        super().__init__()
        self.name = 'Bear'
        self.meal = 'Fish'


class Wolf(Animal):
    def __init__(self):
        super().__init__()
        self.name = 'Wolf'
        self.meal = 'Meat'


bear = Bear()
wolf = Wolf()
animal = (bear, wolf)

for an in animal:
    an.eat()

#8


class City:
    def __new__(cls, name, population):
        if population > 1500:
            return super(City, cls).__new__(cls)
        else:
            print("Your city is too small")

    def __init__(self, name, population):
        self.name = name
        self.population = population


citi_Kyiv = City('Kyiv', 1000)
print(type(citi_Kyiv))

citi_Yaremche = City('Yaremche', 3000)
print(type(citi_Yaremche))
print(citi_Yaremche.name, citi_Yaremche.population)
