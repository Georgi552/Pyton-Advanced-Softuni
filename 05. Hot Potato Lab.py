from  collections import deque
childern = deque(input().split(" "))
counter = int(input()) -1
while len(childern) > 1:
    childern.rotate(-counter)
    print(f"Removed {childern.popleft()}")

print(f"Last is {childern.popleft()}")
