# Працює з інтерпрітатором Python версії 3.10 та вищще, так як використовувалась структура match - case.
#1. Створив нову сутність салон, додав можливість при створенні працівника вказати його Салон по назві Салону
#2.* Вніс все що є в main в окремий клас Controller, за принципом - меню один метод, створення employee окремий метод і т.д. це все в тій ж аплікації.
# Виявив можливі поломки программи, обробив помилки завдяки Try - except та додаванням додаткових перевірок If.
# порефакторів код: виніс повторюємі частини в окрему функцію.

#######
"""
При виконанні домашньої роботи цього разу обробив додаткові виявлені можливі помилки, розібрався з логами та додав їх
в код. Окрім того трохи порефакторив код.
"""
from models.models import Plant, Employee, Salon
import logging

date_strftime_format = "%d-%b-%y %H:%M:%S"
message_format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='logs/main.log', format=message_format,
                    datefmt=date_strftime_format, encoding='UTF-8', level=logging.DEBUG)


class Controller:

    @classmethod
    def main_menu(cls):
        while True:
            print("\n\n"
                  "1. Add new plant \n"
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
            logging.info('Menu printed')
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
                case _: print("\nInvalid input. Select a val    ue from the list\n")

    @classmethod
    def create_plant(cls):
        name = input("Type name of new plant: ")
        location = input("Type location of plant: ")
        plant = Plant(name, location)
        plant.save()
        logging.info('save new Plant')

    @classmethod
    def get_all_plants(cls):
        plants = Plant.get_all()
        for plant in plants:
            print(plant)

    @classmethod
    def get_plant_by_id(cls):
        i = cls.get_int_num_from_user('Type id of plant: ')
        try:
            plant = Plant.get_by_id(i)
            print(plant)
        except ValueError as e:
            logging.error(str(e).format(i, 'Plant'))
            print(str(e).format(i, 'Plant'))

    @classmethod
    def delete_plant_by_id(cls):
        i = cls.get_int_num_from_user('Type id of plant which you want to delete: ')
        Plant.delete(i)
        logging.info('delete Plant')

    @classmethod
    def new_employee(cls):
        name = input("Type name of employee: ")
        email = input("Type email of employee: ")
        plant_id = cls.get_int_num_from_user("Type id of plant: ")
        try:
            salon = Salon.get_salon_from_user()
        except ValueError as e:
            logging.error(e)
            print(e)
            print('Employee do not save. Enter the salon in database')
        else:
            employee = Employee(name, email, plant_id, salon)
            employee.save()
            logging.info('save new Employee')

    @classmethod
    def get_all_employee(cls):
        employees = Employee.get_all()
        for employee in employees:
            print(employee)

    @classmethod
    def get_employee_by_id(cls):
        i = cls.get_int_num_from_user('Type id of employee: ')
        try:
            employee = Employee.get_by_id(i)
            print(employee)
        except ValueError as e:
            logging.error(str(e).format(i, 'Employee'))
            print(str(e).format(i, 'Employee'))

    @classmethod
    def delete_employee_by_id(cls):
        i = cls.get_int_num_from_user('Type id of employee: ')
        Employee.delete(i)
        logging.info('delete Employee')

    @classmethod
    def add_new_salon(cls):
        name = input("CREATE A SALON: \nType name of new salon: ")
        address = input("Type location of address: ")
        salon = Salon(name, address)
        salon.save()
        logging.info('save new Salon')

    @classmethod
    def get_all_salons(cls):
        salons = Salon.get_all()
        for salon in salons:
            print(salon)

    @classmethod
    def get_salon_by_id(cls):
        i = cls.get_int_num_from_user('Type id of salon: ')
        try:
            salon = Salon.get_by_id(i)
            print(salon)
        except ValueError as e:
            logging.error(str(e).format(i, 'Salon'))
            print(str(e).format(i, 'Salon'))

    @classmethod
    def delete_salon_by_id(cls):
        i = cls.get_int_num_from_user('Type id of salon: ')
        Salon.delete(i)
        logging.info('delete Salon')

    @classmethod
    def get_int_num_from_user(cls, text):
        """
        #Цей метод створений щоб прийняти від користувача вибір, в вигляді числа.
        #Якщо користувач вводить не числове значення, відловлюється помилка
        #та рекурсивно функція викликає сама себе для повторного вводу.

        З РОЗРОСТАННЯМ ПРОГРАММИ ЦЕЙ МЕТОД МЕНІ СТАВ ПОТРІБЕН І В МОДЕЛЯХ, ВИРІШИВ ПЕРЕНЕСТИ ЙОГО В БАТЬКІВСЬКИЙ
        КЛАСС, ТА ЗРОБИВ ЙОГО STATICK МЕТОДОМ. ЦЕ МЕНІ ДАЛО ДОСТУП ДО ЦЬОГО МЕТОДА З ВСІЄЇ ПРОГИ.
        В ФАЙЛІ MAIN ОБГОРНУВ ЙОГО В СТАРУ НАЗВУ, ЩОБ МЕНЬШЕ ВИПРАВЛЯТИ КОД І НЕ ІМПОРТУВАТИ ОКРЕМИЙ КЛАС ЗАРАДИ ОДНОГО
        МЕТОДА..
        :param text:
        :return: int
        """
        return Plant.get_int_num_from_user(text)


if __name__ == '__main__':
    Controller.main_menu()

