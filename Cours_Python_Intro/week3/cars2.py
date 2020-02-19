import os
import csv


class BaseCar:
    def __init__(self, car_type, photo_file_name,
                 brand, carrying):
        self.car_type = car_type
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(BaseCar):
    def __init__(self, car_type, photo_file_name,
                 brand, carrying, passenger_seats_count):
        super().__init__(car_type, photo_file_name, brand,
                         carrying)
        self.passenger_seats_count = passenger_seats_count

    def __repr__(self):
        return '{}, {}, {}, {}, {}'.format(
            self.car_type, self.photo_file_name,
            self.brand, self.carrying, self.passenger_seats_count)


class Truck(BaseCar):
        def __init__(self, car_type, photo_file_name,
                     brand, carrying, body_width,
                     body_height, body_length):
            super().__init__(car_type, photo_file_name, brand,
                             carrying)
            self.body_width = body_width
            self.body_height = body_height
            self.body_length = body_length

        def get_body_volume(self):
            return self.body_length * self.body_height * self.body_width


class SpecMachine(BaseCar):
        def __init__(self, car_type, photo_file_name,
                     brand, carrying, extra):
            super().__init__(car_type, photo_file_name, brand,
                             carrying)
            self.extra = extra


def get_car_list(csv_path):
    car_list = []
    if os.path.exists(csv_path) and os.path.getsize(csv_path) > 0:
        with open(csv_path, 'r') as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                if len(row) >= 6:
                    car_type = row[0]
                    brand = row[1]
                    passenger_seats_count = row[2]
                    photo_file_name = row[3]
                    body_whl = row[4]
                    carrying = row[5]
                    extra = row[6]
                if car_type == 'car':
                    car_list.append(
                        create_car(car_type, photo_file_name,
                                   brand, carrying, passenger_seats_count))
                elif car_type == 'truck':
                    if body_whl == '':
                        body_width, body_height, body_length = 0, 0, 0
                    else:
                        body_width = float(body_whl.split('x')[0])
                        body_height = float(body_whl.split('x')[1])
                        body_length = float(body_whl.split('x')[2])
                    car_list.append(create_truck(car_type, photo_file_name,
                                                 brand, carrying, body_width,
                                                 body_height, body_length))
                elif car_type == 'spec_machine':
                    car_list.append(
                        create_spec_machine(car_type, photo_file_name,
                                            brand, carrying, extra))
    return car_list


def create_car(car_type, photo_file_name,
               brand, carrying, passenger_seats_count):
    return Car(car_type, photo_file_name,
               brand, carrying, passenger_seats_count)


def create_truck(car_type, photo_file_name,
                 brand, carrying, body_width,
                 body_height, body_length):

    return Truck(car_type, photo_file_name,
                 brand, carrying, body_width,
                 body_height, body_length)


def create_spec_machine(car_type, photo_file_name,
                        brand, carrying, extra):

    return SpecMachine(car_type, photo_file_name,
                       brand, carrying, extra)

'''
L = []
L.append(Car(123, 123, 123, 123, 12))
print(L)
'''
if __name__ == '__main__':
    print(get_car_list('coursera_week3_cars.csv'))
