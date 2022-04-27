def even_odd(*args):
    result = []
    comand = args[len(args) - 1]
    if comand == "even":
        for i in range(len(args) -1):
            if int(args[i]) % 2 == 0:
                result.append(args[i])

    elif comand == "odd":
        for i in range(len(args) - 1):
            if not int(args[i]) % 2 == 0:
                result.append(args[i])

    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))