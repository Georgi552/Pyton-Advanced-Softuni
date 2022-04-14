from collections import deque
queue = deque()
while True:
    comand = input()
    if comand == "Paid":
        while len(queue):
            print(queue.popleft())
    elif comand == "End":
        print(f"{len(queue)} people remaining.")
        break
    else:
        queue.append(comand)