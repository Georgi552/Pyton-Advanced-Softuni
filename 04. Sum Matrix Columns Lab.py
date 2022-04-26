row_length, column_lengt = [int(i) for i in input().split(", ")]

matrix = []

for i in range(row_length):
    row = [int(el) for el in input().split(" ")]
    matrix.append(row)

matrix_reversed = []
for i in range(column_lengt):
    row_reversed = []
    for x in range(row_length):
        row_reversed.append(matrix[x][i])
    matrix_reversed.append(row_reversed)



for r in matrix_reversed:
    print(sum(r))
