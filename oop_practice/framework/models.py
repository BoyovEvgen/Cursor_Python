import json
from abc import ABC
import os
import logging


class Model(ABC):
    file = "default.json"

    @staticmethod
    def get_data(path):
        try:
            file = open(path, "r")
            data = json.loads(file.read())
            file.close()
        except FileNotFoundError as e:
            logging.warning(e)
            if not os.path.exists("database"):
                os.mkdir("database")
            with open(path, 'w+') as file:
                file.write('[]')
                file.seek(0)
                data = json.loads(file.read())
        return data

    def save(self):
        data = self.get_data("database/" + self.file)
        new_instance = self.__dict__
        if len(data) > 0:
            new_instance["id"] = data[-1]["id"] + 1
        else:
            new_instance["id"] = 1
        data.append(new_instance)
        self.save_data_to_file(data, "database/" + self.file)

    @staticmethod
    def save_data_to_file(data, path):
        try:
            file = open(path, "w")
            file.write(json.dumps(data))
            file.close()
        except FileNotFoundError as e:
            logging.warning(e)
            if not os.path.exists("database"):
                logging.warning("Folder database don't exist")
                os.mkdir("database")

            with open(path, "w") as file:
                file.write(json.dumps(data))
                logging.info("File created")

    @classmethod
    def get_all(cls):
        instances = cls.get_data("database/" + cls.file)
        return instances

    @classmethod
    def get_by_id(cls, id):
        instances = cls.get_data("database/" + cls.file)
        for instance in instances:
            if instance["id"] == id:
                return instance
        raise ValueError("Id {} is not in database {}")

    @classmethod
    def delete(cls, id):
        instances = cls.get_data("database/" + cls.file)
        for i in range(len(instances)):
            if instances[i]["id"] == id:
                del instances[i]
                break
        cls.save_data_to_file(instances, "database/" + cls.file)

    @staticmethod
    def get_int_num_from_user(text):
        """
        Цей метод створений щоб прийняти від користувача вибір, в вигляді числа.
        Якщо користувач вводить не числове значення, відловлюється помилка
        та рекурсивно функція викликає сама себе для повторного вводу.
        :param text:
        :return: int
        """
        try:
            res = int(input(text))
            return res
        except ValueError as e:
            logging.error(e)
            print('\nInput error. Enter a numeric value\n')
            return Model.get_int_num_from_user(text)
