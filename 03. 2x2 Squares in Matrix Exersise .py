n_rows, n_colums = input().split(" ")

matrix = []
for i in range(int(n_rows)):
    row = [x for x in input().split(" ")]
    matrix.append(row)
n_rows = int(n_rows)
n_colums = int(n_colums)
x = 0
y = 0
similar_counter = 0
corrent_matrix = []
corrent_row_1 = []
corrent_row_2 = []
for i in range((n_rows - 1) * (n_colums - 1)):
    corrent_matrix = []
    corrent_row_1 = []
    corrent_row_2 = []
    t = 0
    if y >= (n_colums - 1):
        y = 0
        x += 1
    for r in range(0 + x, 2 + x):
        for c in range(0 + y, 2 + y):
            if t < 2:
                corrent_row_1.append(matrix[r][c])
                t += 1
            else:
                corrent_row_2.append(matrix[r][c])

        corrent_matrix.append(corrent_row_1)
    y += 1

    if corrent_row_1 == corrent_row_2:
        if corrent_row_1[0] == corrent_row_1[1]:
            similar_counter += 1

print(similar_counter)


