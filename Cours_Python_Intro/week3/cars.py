import os
import csv


class BaseCar:
    def __init__(self, photo_file_name,
                 brand, carrying):

        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying
        self.car_type = None

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(BaseCar):
    def __init__(self, photo_file_name,
                 brand, carrying, passenger_seats_count):
        super().__init__(photo_file_name, brand,
                         carrying)
        self.passenger_seats_count = passenger_seats_count
        self.car_type = 'car'

"""    
def __repr__(self):
        return '{}, {}, {}, {}, {}'.format(
            self.car_type, self.photo_file_name,
            self.brand, self.carrying, self.passenger_seats_count)
"""


class Truck(BaseCar):
        def __init__(self, photo_file_name,
                     brand, carrying, body_whl):
            super().__init__(photo_file_name, brand,
                             carrying)
            self.body_whl = body_whl
            if body_whl == '':
                self.body_width = 0.0
                self.body_height = 0.0
                self.body_length = 0.0
            else:
                self.body_width = float(self.body_whl.split('x')[0])
                self.body_height = float(self.body_whl.split('x')[1])
                self.body_length = float(self.body_whl.split('x')[2])
            self.car_type = 'truck'

        def get_body_volume(self):
            return self.body_length * self.body_height * self.body_width


class SpecMachine(BaseCar):
        def __init__(self, photo_file_name,
                     brand, carrying, extra):
            super().__init__(photo_file_name, brand,
                             carrying)
            self.extra = extra
            self.car_type = 'spec_machine'


def get_car_list(csv_path):
    car_list = []
    if os.path.exists(csv_path) and os.path.getsize(csv_path) > 0:
        with open(csv_path, 'r') as f:
            reader = csv.reader(f, delimiter=';')
            next(reader)
            for row in reader:
                if len(row) == 7:
                    if row[0] == 'car':
                        tmp = Car(brand=row[1], passenger_seats_count=int(row[2]), photo_file_name=row[3], carrying=float(row[5]))
                        car_list.append(tmp)
                    elif row[0] == 'truck':
                        tmp = Truck(brand=row[1], photo_file_name=row[3], body_whl=row[4], carrying=float(row[5]))
                        car_list.append(tmp)
                    elif row[0] == 'spec_machine':
                        tmp = SpecMachine(brand=row[1], photo_file_name=row[3], carrying=float(row[5]), extra=row[6])
                        car_list.append(tmp)
    return car_list


'''
L = []
L.append(Car(123, 123, 123, 123, 12))
print(L)
'''
if __name__ == '__main__':
    print(get_car_list('coursera_week3_cars.csv'))
