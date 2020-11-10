class Car:

    def __init__(self,  model, color, doors, wheels):
        self.model = model
        self.doors = doors
        self.wheels = wheels
        self.color = color

    def drive(self):
        print('Машина поехала!!!')

    def brake(self):
        print('Машина остановилась!!!')

class Truck(Car):

    def __init__(self, capacity):
        self.capacity = capacity

    def unload(self):
        print('Выгрузка груза...')

class Passenger_car(Car):

    def open_trunk(self):
        print('Багажник открыт.')