from framework.models import Model


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


class Salon(Model):
    file = "salon.json"

    def __init__(self, name, address):
        self.name = name
        self.address = address

