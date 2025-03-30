class Motor:

    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
        self.capacity = 50

class Trunk:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.weight = 60


class Auto(Motor, Trunk):

    def print_info(self):
        print(f'Model of car: {self.model}')
        print(f'Capacity of motor: {self.capacity}')
        print(f'Weigh of baggage: {self.weight}')

auto = Auto(model = 'BMW')
auto.print_info()
