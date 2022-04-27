comand = input()
num = [int(el) for el in input().split(" ")]
result = 0
if comand == "Even":
    for el in num:
        if el % 2 == 0:
            result += el

    print(result * len(num))

if comand == "Odd":
    for el in num:
        if not el % 2 == 0:
            result += el
    print(result * len(num))