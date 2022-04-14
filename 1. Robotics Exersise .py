def time_plus_sec(time, aditional_second):
    timex = str(time).split(":")

    sec = int(timex[2])
    min = int(timex[1])
    hour = int(timex[0])

    sec += int(aditional_second)
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

    if sec < 10:
        if min < 10:
            if hour < 10:
                return(f"0{hour}:0{min}:0{sec}")
            else:
                return(f"{hour}:0{min}:0{sec}")
        else:
            return(f"{hour}:{min}:0{sec}")
    elif sec > 10:
        if min < 10:
            if hour < 10:
                return(f"0{hour}:0{min}:{sec}")
            else:
                return(f"{hour}:0{min}:{sec}")
        else:
            return(f"0{hour}:{min}:{sec}")

    elif hour > 10:
        if min < 10:
            if sec < 10:
                return(f"{hour}:0{min}:0{sec}")
            else:
                return(f"{hour}:{min}:0{sec}")
        else:
            return(f"{hour}:{min}:{sec}")


def time_comparison(clock1, clock2):
    time1 = str(clock1).split(":")
    time2 = str(clock2).split(":")

    if int(time1[0]) == int(time2[0]) and int(time1[1]) == int(time2[1]) and int(time1[2] > time2[2]):
        return True

    elif int(time1[0]) == int(time2[0]) and int(time1[1]) > int(time2[1]):
        return True

    elif int(time1[0]) > int(time2[0]):
        return True

    else:
        return False


robots = input().split(";")
start_time = input()
new_robots = []
for el in robots:
    new_robots.append(el.split("-"))
#dict_robots = {}
#for i in range(len(new_robots)):
#    key = new_robots[i][0]
#    value = new_robots[i][1]
 #   dict_robots[key] = value


busy_robots = {}
current_time = time_plus_sec(start_time, 1)
detail = input()
detail_counter = 0
if detail_counter >= len(robots) - 1:
    detail_counter = 0
while not detail == "End":
    for i in range(len(robots)):
        if detail_counter >= len(robots):
            detail_counter = 0
            i = detail_counter
        i = detail_counter

        robot_name = robots[i]
        if len(busy_robots) < len(robots):
            availabe_at = start_time
            busy_robots[robot_name] = availabe_at
        else:
            for availabe_at, robot_name in busy_robots.items():
                if robot_name == robots[i]:
                    rob_aval_at = availabe_at
        rob_aval_at = availabe_at
        available = time_comparison(current_time, rob_aval_at)
        if available is True:
            print(f"{robot_name} - {detail} {current_time}")
            robot_availabe_at = time_plus_sec(current_time, new_robots[i][1])
            busy_robots[robot_name] = robot_availabe_at
            current_time = time_plus_sec(current_time, 1)
            i += 1
            break
        else:
            continue

    detail_counter += 1
    detail = input()

print(current_time)