from collections import deque
queue_people = deque()
water_Liters = int(input())
name = input()
while not name == "Start":
    queue_people.append(name)
    name = input()

comand = input()
queue_comands = deque()
while not comand == "End":
    if "refill" in comand:
        comand_list = comand.split(" ")
        water_Liters += int(comand_list[1])
    else:
        liters = int(comand)
        if liters <= water_Liters:
            print(f"{queue_people.popleft()} got water")
            water_Liters -= liters
        else:
            print(f"{queue_people.popleft()} must wait")

    comand = input()
if comand == "End":
    print(f" {water_Liters} liters left")

