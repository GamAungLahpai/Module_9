from module9 import Car
import random

# Create a list of 10 cars
cars = []
for i in range(10):
    cars.append(Car("ABC-" + str(i + 1), random.randint(100, 200)))

distance_max = 0


while distance_max < 10000:
    for car in cars:
        # Adjust speed randomly between -10 and +15
        car.accelerate(random.randint(-10, 15))
        # Drive for one hour
        car.drive(1)
        distance_max = max(car.travelled_distance, distance_max)



for car in cars:
    print(f"{car.registration_number},: {car.maximum_speed}, {car.current_speed}, {car.travelled_distance}")
