import os
import csv


class BaseCar:

	def __init__(self, photo_file_name, car_type, brand, carrying):
		try:
			self.photo_file_name = photo_file_name
			self.car_type = car_type
			self.brand = brand	
			self.carrying = float(carrying)
		except:
			print('BaseCar_init error')

	def get_photo_file_ext(self):
		try:
			return os.path.splitext(self.photo_file_name)[1]
		except:
			print('class BaseCar, get_photo_file_ext error')


class Car(BaseCar):

	def __init__(self, photo_file_name, car_type, brand, carrying, passenger_seats_count):
		try:
			super().__init__(photo_file_name, car_type, brand, carrying)
			self.passenger_seats_count = int(passenger_seats_count)
		except:
			print('Car_init error')


class Truck(BaseCar):
	
	def __init__(self, photo_file_name, car_type, brand, carrying, body_width, body_height, body_length):
		try:
			super().__init__(photo_file_name, car_type, brand, carrying)
			self.body_width = float(body_width)
			self.body_height = float(body_height)
			self.body_length = float(body_length)
		except:
			print('Truck_init error')

	def get_body_volume(self):
		try:
			return self.body_width*self.body_height*self.body_length
		except:
			print('class Truck, get_body_volume error')


class SpecMachine(BaseCar):

	def __init__(self, photo_file_name, car_type, brand, carrying, extra):
		try:
			super().__init__(photo_file_name, car_type, brand, carrying)
			self.extra = extra
		except:
			print('SpecMachine_init error')

def size_split(size):
	try:
		if size == '':
			return [0, 0, 0]
		else:
			digit_size = [float(i) for i in size.split("x")]
			return digit_size
	except:
		print('size_split error')


def car_creation(row):
	try:
		return Car(row[3], row[0], row[1], row[5], row[2])
	except:
		print('car_creation error')


def truck_creation(row):
	try:
		digit_size = size_split(row[4])
		return Truck(row[3], row[0], row[1], row[5], digit_size[1], digit_size[2], digit_size[0])
	except:
		print('truck_creation error')


def specmachine_creation(row):
	try:
		return SpecMachine(row[3], row[0], row[1], row[5], row[6])
	except:
		print('spec_machine_creation error')


def get_car_list(file_name):
	try:
		car_list = []
		with open(file_name) as fd:
			reader = csv.reader(fd, delimiter = ';')
			next(reader)
			for row in reader:
				if len(row) == 7:
					if row[0] == 'car':
						car_list.append(car_creation(row))
					elif row[0] == 'truck':
						car_list.append(truck_creation(row))
					elif row[0] == 'spec_machine':	
						car_list.append(specmachine_creation(row))	
					else:
						print('incorrect size')
						break
				else:
					continue
		return car_list
	except:
		print('get_car_list error')
		
