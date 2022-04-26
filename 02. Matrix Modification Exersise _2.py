n_rows = int(input())

matrix = []
for i in range(n_rows):
    row = input().split(" ")
    matrix.append(row)

comand = input()

while not comand == "END":
    comands = comand.split(" ")
    action = comands[0]
    current_row = int(comands[1])
    colum = int(comands[2])
    number = int(comands[3])
    if 0 <= current_row < n_rows and 0 <= colum < len(row):

        if action == "Add":
            matrix[current_row][colum] = int(matrix[current_row][colum]) + int(number)

        if action == "Subtract":
            matrix[current_row][colum] = int(matrix[current_row][colum]) - int(number)

    else:
        print(f"Invalid coordinates")


    comand = input()

for i in range(n_rows):
    print(f"{' '.join(map(str, matrix[i]))}")