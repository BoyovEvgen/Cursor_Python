from framework.models import Model
import logging


class Plant(Model):
    file = "plants.json"

    def __init__(self, name, location):
        self.name = name
        self.location = location


class Employee(Model):
    file = "employees.json"

    def __init__(self, name, email, plant_id, salon):
        self.name = name
        self.email = email
        self.plant_id = plant_id
        self.salon = salon

    def check_email(self):
        data = self.get_all()
        for el in data:
            if self.email == el["email"]:
                raise ValueError("This email already exist!")

    def check_email_format(self):
        if not "@" in self.email or not "." in self.email:
            raise ValueError("Not a valid email address!")
        position = self.email.find("@")
        position_of_dot = self.email.find(".")
        if position > position_of_dot:
            raise ValueError("Not a valid email address!")

    def save(self):
        try:
            plant = Plant.get_by_id(self.plant_id)
        except ValueError as e:
            logging.error(str(e).format(self.plant_id, 'Plant'))
            print("You need to write a plant_id of existing plant!")
            print('Employee do not save')
            return
        try:
            self.check_email()
            self.check_email_format()
        except ValueError as e:
            logging.error(str(e) + " Email: " + self.email)
            print(e)
            print('Employee do not save')
            return
        super().save()


class Salon(Model):
    file = "salon.json"

    def __init__(self, name, address):
        self.name = name
        self.address = address

    @classmethod
    def get_salon_from_user(cls):
        """"
        ПЕРЕНІС ЙОГО СЮДИ, ТАК Я ВІДНОСИТЬСЯ Ж ВІН ДО SALON БІЛЬШЕ НІЖ ДО KONTROLLER :)

        цей метод виводить імена салонів занесених в нашу базу,
        питає користувача який вибрати,
        та повертає вибране ім'я салона.
        """
        cls.check_salon_in_database()
        salons = cls.get_all()
        salon_name = [salon['name'] for salon in salons]
        print('Select a salon from the existing one in the database')
        for i in range(1, len(salon_name)+1):
            print(f'{i}. {salon_name[i-1]}')
        i = Model.get_int_num_from_user('Enter the salon number for the employee: ')
        try:
            name = salon_name[i-1]
            return name
        except IndexError as e:
            logging.error(str(e) + " Invalid input salon number")
            print("\nInvalid input. Select a value from the list\n")
            return cls.get_salon_from_user()

    @classmethod
    def check_salon_in_database(cls):
        salons = Salon.get_all()
        if len(salons) < 1:
            raise ValueError('Database SALON is empty')

