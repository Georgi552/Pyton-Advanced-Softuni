n = int(input())
car_register = set()
for i in range(n):
    comand = input().split(", ")
    direction = comand[0]
    car_plate = comand[1]
    if direction == "IN":
        car_register.add(car_plate)
    if direction == "OUT":
        car_register.remove(car_plate)

if len(car_register) > 0:
    for plate in car_register:
        print(plate)
else:
    print(f"Parking Lot is Empty")