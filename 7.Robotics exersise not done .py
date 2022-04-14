from collections import deque
queue = deque()

time = input().split(":")
aditional_second = int(input())

def time_plus_sec(time, aditional_second)


    sec = int(time[2])
    min = int(time[1])
    hour = int(time[0])

    sec += aditional_second
    if sec > 59:
        while sec > 59:
            sec -= 60
            min += 1
    if min > 59:
        while min > 59:
            min -= 60
            hour += 1
    if hour > 24:
        while hour > 24:
            hour -= 24
            min = 0
            sec = 0
    print(f"{hour}:{min}:{sec}")
    if sec < 10:
        if min < 10:
            if hour < 10:
                print(f"0{hour}:0{min}:0{sec}")
            else:
                print(f"{hour}:0{min}:0{sec}")
        else:
            print(f"{hour}:{min}:0{sec}")
    elif sec > 10:
        if min < 10:
            if hour < 10:
                print(f"0{hour}:0{min}:{sec}")
            else:
                print(f"{hour}:0{min}:{sec}")
        else:
            print(f"0{hour}:{min}:{sec}")

    elif hour > 10:
        if min < 10:
            if sec < 10:
                print(f"{hour}:0{min}:0{sec}")
            else:
                print(f"{hour}:{min}:0{sec}")
        else:
            print(f"{hour}:{min}:{sec}")



robots = input().split(";")
start_time = input().split(":")
details = input()
robots_list = []

robot_names = []
robot_times = []
for i in range(len(robots)):
    robots_list.append(robots[i].split("-"))

for robo in robots_list:
    robot_names.append(robo[0])
    robot_times.append(robo[1])


while not details == "End":







    details = input()
print(robot_time)



time = input().split(":")
time_int = []
aditional_second = int(input())
for el in time:
    time_int.append(int(el))

time_int[2] += aditional_second
if int(time_int[2]) > 59:
    (time_int[2]) -= 60
    (time_int[1]) += 1


print(f"{'-'.join(str(time_int))}")


