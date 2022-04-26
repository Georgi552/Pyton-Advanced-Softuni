n_rows, n_colums = input().split(" ")
n_rows, n_colums = int(n_rows), int(n_colums)

matrix = []
for i in range(n_rows):
    row = [(el) for el in input().split(" ")]
    matrix.append(row)

comand1 = input()
while not comand1 == "END":

    comand = comand1.split(" ")
    if len(comand) == 5 and comand[0] == "swap" and int(comand[1]) <= n_rows and int(
            comand[2]) <= n_colums and int(comand[3]) <= n_rows and int(comand[4]) <= n_colums:
        matrix[int(comand[1])][int(comand[2])], matrix[int(comand[3])][int(comand[4])] = matrix[int(
            comand[3])][int(comand[4])], matrix[int(comand[1])][int(comand[2])]
        for r in range(n_rows):
            pr_row = []
            for c in range(n_colums):
                pr_row.append(matrix[r][c])

            print(' '.join(map(str, pr_row)))

    else:
        print(f"Invalid input!")
    comand1 = input()