from module9 import Car

car1 = Car ("ABC - 123",142)

print(f"""
Registration number: {car1.registration_number}
Maximum speed : {car1.maximum_speed}
Current speed : {car1.current_speed}
Travelled distance : {car1.travelled_distance}
""")

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)

print (f"Current speed : {car1.current_speed}km/h")

car1.accelerate(-200)
print (f"Current speed : {car1.current_speed}km/h")

car1.accelerate(50)
car1.drive(1.5)
print(f" Travelled distance : {car1.travelled_distance}km")