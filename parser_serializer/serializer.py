import datetime
import json
import csv


class Human:
    def __init__(self, name, surname, age, birth_date=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.birth_date = birth_date or datetime.datetime.now()


class HumanSerializer:
    @staticmethod
    def serialize(obj, format):
        data = obj.__dict__.copy()
        if format == 'json':
            HumanSerializer._serialize_to_json(data)
        elif format == 'csv':
            HumanSerializer._serializer_to_csv(data)

    @staticmethod
    def _serialize_to_json(data):
        data['birth_date'] = data['birth_date'].strftime("%d-%m-%Y %H:%M:%S")
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def _serializer_to_csv(data):
        data['birth_date'] = data['birth_date'].strftime("%Y-%m-%d")
        with open('data.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames=list(data.keys()), quoting=csv.QUOTE_NONNUMERIC)
            writer.writeheader()
            writer.writerow(data)


obj = Human('Evhen', 'Boiov', 30, datetime.date(1992, 12, 1))

HumanSerializer.serialize(obj=obj, format='csv')
HumanSerializer.serialize(obj=obj, format='json')


