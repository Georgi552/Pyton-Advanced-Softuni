from collections import deque
expression = input().split()

result = deque(expression)
current_nums = []
for i in range(len(expression)):
    if expression[i].isdigit() or expression[i].startswith("-") and expression[i][1:].isdigit():
        current_nums.append(expression[i])
        result.remove(expression[i])

    if not expression[i].isdigit():
        if expression[i] == "+":
            el = int(current_nums[0])
            for x in range(1, len(current_nums)):
                el = el + int(current_nums[x])
            current_nums = []
            current_nums.append(el)
            result.remove(expression[i])

        if expression[i] == "-":
            el = int(current_nums[0])
            for x in range(1, len(current_nums)):
                el = el - int(current_nums[x])
            current_nums = []
            current_nums.append(el)
            result.remove(expression[i])

        if expression[i] == "*":
            el = int(current_nums[0])
            for x in range(1, len(current_nums)):
                el = el * int(current_nums[x])
            current_nums = []
            current_nums.append(el)
            result.remove(expression[i])

        if expression[i] == "/":
            el = int(current_nums[0])
            for x in range(1, len(current_nums)):
                el = el / int(current_nums[x])
            current_nums = []
            current_nums.append(el)
            result.remove(expression[i])


print(round(*current_nums))



