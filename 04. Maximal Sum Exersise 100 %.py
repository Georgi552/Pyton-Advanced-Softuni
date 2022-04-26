n_rows, n_colums = input().split(" ")

matrix = []
for i in range(int(n_rows)):
    row = [x for x in input().split(" ")]
    matrix.append(row)
n_rows = int(n_rows)
n_colums = int(n_colums)
biggest_matrix_sum = 0
biggest_row_1 = []
biggest_row_2 = []
biggest_row_3 = []

current_matrix_sum = 0
current_row_1 = []
current_row_2 = []
current_row_3 = []

checked_matrixes = 0
x = 0
y = 0
counter = 0
while checked_matrixes < ((n_rows - 2) * (n_colums - 2)):
    current_matrix_sum = 0
    current_row_1 = []
    current_row_2 = []
    current_row_3 = []
    colum = 0
    if y + 3 > n_colums:
        y = 0
        x += 1
    colum = 0
    for r in range(0 + x, 3 + x):
        for c in range(0 + y, 3 + y):
            if colum < 3:
                current_row_1.append(matrix[r][c])
                colum += 1
            elif 3 <= colum < 6:
                current_row_2.append(matrix[r][c])
                colum += 1
            elif 6 <= colum < 9:
                current_row_3.append(matrix[r][c])
                colum += 1
                counter += 1

    checked_matrixes += 1
    y += 1
    row_1_sum = sum([int(el) for el in current_row_1])
    row_2_sum = sum([int(el) for el in current_row_2])
    row_3_sum = sum([int(el) for el in current_row_3])

    current_matrix_sum = row_1_sum + row_3_sum + row_2_sum
    if current_matrix_sum >= biggest_matrix_sum:
        biggest_matrix_sum = current_matrix_sum
        biggest_row_1 = current_row_1
        biggest_row_2 = current_row_2
        biggest_row_3 = current_row_3


print(f"Sum = {biggest_matrix_sum}")
print(f"{' '.join(map(str, biggest_row_1))}")
print(f"{' '.join(map(str, biggest_row_2))}")
print(f"{' '.join(map(str, biggest_row_3))}")


