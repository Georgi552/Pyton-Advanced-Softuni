first = [int(el) for el in input().split()]
second = [int(el) for el in input().split()]
first = set(first)
second = set(second)

n_comands = int(input())

for i in range(n_comands):
    command = input().split()

    if command[0] == "Add":
        if command[1] == "First":
            for i in range(2, len(command)):
                first.add(int(command[i]))
        if command[1] == "Second":
            for x in range(2, len(command)):
                second.add(int(command[x]))
        else:
            pass

    elif command[0] == "Remove":
        if command[1] == "First":
            for y in range(2, len(command)):
                if int(command[y]) in first:
                    first.remove(int(command[y]))
        if command[1] == "Second":
            for z in range(2, len(command)):
                if int(command[z]) in second:
                    second.remove(int(command[z]))
        else:
            pass

    elif command[0] == "Check":
        if first.issubset(second):
            print('True')
        elif second.issubset(first):
            print('True')
        else:
            print('False')
    else:
        pass

first = sorted(first)
second = sorted(second)

print(', '.join(map(str, first)))
print(', '.join(map(str, second)))
