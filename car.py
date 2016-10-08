class Car():
    def __init__(self, name='General', model='GM', num_of_doors=4, num_of_wheels=4, vehicle_type='saloon', speed=0):
        self.vehicle_type = vehicle_type
        self.name = name
        self.model = model
        if name == 'Porshe' or name == 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4
        if vehicle_type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4
        self.speed = speed

    def is_saloon(self):
        if self.vehicle_type == 'saloon':
            return True
        else:
            return False

    def drive(self, spd):
        if self.vehicle_type == 'trailer':
            self.speed = 77
        else:
            self.speed = 1000
        return self
