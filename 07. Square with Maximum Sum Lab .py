n_rows, n_colums = [int(el) for el in input().split(", ")]

matrix = []
for r in range(n_rows):
    row = [int(el) for el in input().split(", ")]
    matrix.append(row)
biggest_matrix = []

current_list_matrix = []
biggest_list_matrix = []

biggest_sum = 0
current_sum = 0
counter = 0
i = 0
x = 0
while counter < ((n_rows - 1) * (n_colums - 1)):
    current_sum = 0
    current_list_matrix =[]
    current_row_2 =[]

    if i >= n_colums - 1:
        i = 0
        x += 1

    for r in range(0 + x, 2 + x):

        for c in range(0 + i , 2 + i):
            current_element = matrix[r][c]
            current_sum += current_element
            current_list_matrix.append(current_element)

    i += 1

    counter += 1
    if current_sum > biggest_sum:
        biggest_sum = current_sum
        biggest_list_matrix = current_list_matrix
new_row1 = []
new_row2 = []
for i in range(4):
    if i in range(0, 2):
        new_row1.append(biggest_list_matrix[i])
    if i in range(2, 4):
        new_row2.append(biggest_list_matrix[i])
biggest_matrix.append(new_row1)
biggest_matrix.append(new_row2)


print(f"{new_row1[0]} {new_row1[1]}")
print(f"{new_row2[0]} {new_row2[1]}")
print(biggest_sum)
