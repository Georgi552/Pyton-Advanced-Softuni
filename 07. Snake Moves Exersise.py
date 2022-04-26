def create_blank_matrix(row_size, col_size):
    matrix = []
    for i in range(row_size):
        row = ["" for el in range(col_size)]
        matrix.append(row)
    return (matrix)

n_rows, n_colums = input().split(" ")
n_rows, n_colums = int(n_rows), int(n_colums)
text = input()


text_index = 0

matrix = create_blank_matrix(n_rows ,  n_colums)

col = 0
for row in range(n_rows):

    if row % 2 == 0:
        direction = 1
    else:
        direction = -1

    while 0 <= col < n_colums:
        matrix[row][col] = text[text_index]

        if text_index + 1 == len(text):
            text_index = -1
        text_index += 1
        col += direction

    col -= direction

for i in range(len(matrix)):
    print(''.join(matrix[i]))

