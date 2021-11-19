class Car:
	car_count = 0
	
	def start(self, model, make, year, color):
		print("Engine started")
		model = self.model
		make = self.make
		year = self.year
		color = self.color
		Car.car_count += 1

	def stop():
		print("Engine stopped")

def switch_gear(gear):
	print(f"Gear shifted to {gear}")

def push_break(procent):
	print(f"Brake pedal depressed {procent} procent")


romas_car = Car()
romas_car.year = 2019
romas_car.model = "G63"
romas_car.make = "Mersedes"
romas_car.color = "Black"

def brabus_switch_gear_box():
	gear_box = "Brabus gear box"
	return gear_box

def brake_brambo():
	brake_model = "Brambo"
	return brake_model

for el in range(1, 7):
	switch_gear(el)
	el += 1

i = 0
for el in range(0, 5):
	push_break(i)
	i += 25
	if el == 4:
		print(switch_gear("neutral"), Car.stop())

print("Time to tunnig")

romas_car.gear_box = brabus_switch_gear_box()
romas_car.brake_model = brake_brambo()

print(f"We have installed the brake improvement by type {romas_car.brake_model}")
print(f"We have installed an improved transmission type {romas_car.gear_box}")


