import sys
n = int(input())
stack = []
stack_reverse = []
while n > 0:
    comand = input().split()
    n -= 1

    if comand[0] == "1":
        if int(comand[1]) <= 109:
            stack.append(comand[1])

    elif comand[0] == "2":
        if len(stack) > 0:
            stack.pop()
        else:
            continue

    elif comand[0] == "3":
        if len(stack) > 0:
            print(max(stack))

    elif comand[0] == "4":
        if len(stack):
            print(min(stack))

if n == 0:
    while len(stack):
        stack_reverse.append(stack.pop())
print(", ".join(stack_reverse))