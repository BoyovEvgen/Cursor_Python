# Працює з інтерпрітатором Python версії 3.10 та вищще, так як використовувалась структура match - case.
#1. Створив нову сутність салон, додав можливість при створенні працівника вказати його Салон по назві Салону
#2.* Вніс все що є в main в окремий клас Controller, за принципом - меню один метод, створення employee окремий метод і т.д. це все в тій ж аплікації.
# Виявив можливі поломки программи, обробив помилки завдяки Try - except та додаванням додаткових перевірок If.
# порефакторів код: виніс повторюємі частини в окрему функцію.
from models.models import Plant, Employee, Salon


class Controller:

    @classmethod
    def main_menu(cls):
        while True:
            print("1. Add new plant \n"
                  "2. Get all plants\n"
                  "3. Get plant by id\n"
                  "4. Delete plant by id\n"
                  "5. Add new employee\n"
                  "6. Get all employee\n"
                  "7. Get employee by id\n"
                  "8. Delete employee by id\n"
                  "9. Add new salon\n"
                  "10. Get all salon\n"
                  "11. Get salon by id\n"
                  "12. Delete salon by id\n"
                  "To stop the program type 'exit'\n"
                  )
            flag = input("Choose: ")
            match flag:
                case '1':
                    cls.create_plant()
                case '2':
                    cls.get_all_plants()
                case '3':
                    cls.get_plant_by_id()
                case '4':
                    cls.delete_plant_by_id()
                case '5':
                    cls.new_employee()
                case '6':
                    cls.get_all_employee()
                case '7':
                    cls.get_employee_by_id()
                case '8':
                    cls.delete_employee_by_id()
                case '9':
                    cls.add_new_salon()
                case '10':
                    cls.get_all_salons()
                case '11':
                    cls.get_salon_by_id()
                case '12':
                    cls.delete_salon_by_id()
                case 'exit':
                    break
                # case 'debug':
                #     print(cls.get_salon_from_user())
                case _: print("\nInvalid input. Select a value from the list\n")

    @classmethod
    def create_plant(cls):
        name = input("Type name of new plant: ")
        location = input("Type location of plant: ")
        plant = Plant(name, location)
        plant.save()

    @classmethod
    def get_all_plants(cls):
        plants = Plant.get_all()
        for plant in plants:
            print(plant)

    @classmethod
    def get_plant_by_id(cls):
        i = cls.get_int_num_from_user('Type id of plant: ')
        plant = Plant.get_by_id(i)
        print(plant)

    @classmethod
    def delete_plant_by_id(cls):
        i = cls.get_int_num_from_user('Type id of plant which you want to delete: ')
        Plant.delete(i)

    @classmethod
    def new_employee(cls):
        name = input("Type name of employee: ")
        email = input("Type email of employee: ")
        plant_id = cls.get_int_num_from_user("Type id of plant: ")
        salon = cls.get_salon_from_user()
        employee = Employee(name, email, plant_id, salon)
        employee.save()

    @classmethod
    def get_all_employee(cls):
        employees = Employee.get_all()
        for employee in employees:
            print(employee)

    @classmethod
    def get_employee_by_id(cls):
        i = cls.get_int_num_from_user('Type id of employee: ')
        employee = Employee.get_by_id(i)
        print(employee)

    @classmethod
    def delete_employee_by_id(cls):
        i = cls.get_int_num_from_user('Type id of employee: ')
        Employee.delete(i)

    @classmethod
    def add_new_salon(cls):
        name = input("Type name of new salon: ")
        address = input("Type location of address: ")
        salon = Salon(name, address)
        salon.save()

    @classmethod
    def get_all_salons(cls):
        salons = Salon.get_all()
        for salon in salons:
            print(salon)

    @classmethod
    def get_salon_by_id(cls):
        i = cls.get_int_num_from_user('Type id of salon: ')
        salon = Salon.get_by_id(i)
        print(salon)

    @classmethod
    def delete_salon_by_id(cls):
        i = cls.get_int_num_from_user('Type id of salon: ')
        Salon.delete(i)

    @classmethod
    def get_int_num_from_user(cls, text):
        """
        Цей метод створений щоб прийняти від користувача вибір, в вигляді числа.
        Якщо користувач вводить не числове значення, відловлюється помилка
        та рекурсивно функція викликає сама себе для повторного вводу.
        :param text:
        :return: int
        """
        try:
            return int(input(text))
        except ValueError:
            print('\nInput error. Enter a numeric value\n')
            return cls.get_int_num_from_user(text)

    @classmethod
    def get_salon_from_user(cls):
        """"
        цей метод виводить імена салонів занесених в нашу базу,
        питає користувача який вибрати,
        та повертає вибране ім'я салону.
        """
        salons = Salon.get_all()
        salon_name = [salon['name'] for salon in salons]
        print('Select a salon from the existing one in the database')
        for i in range(1, len(salon_name)+1):
            print(f'{i}. {salon_name[i-1]}')
        i = cls.get_int_num_from_user('Enter the number: ')
        try:
            name = salon_name[i-1]
            return name
        except IndexError:
            print("\nInvalid input. Select a value from the list\n")
            return cls.get_salon_from_user()


if __name__ == '__main__':
    Controller.main_menu()

