matrix = []

for i in range(3):
    row = []
    for i in range(4):
        row.append(0)
    matrix.append(row)
print(matrix)


matrix_easy = []

for i in range(3):
    matrix_easy.append([0] * 4)
print(matrix_easy)


matrix_comprihension = [[0] * 4 for i in range(3)]
print(matrix_comprihension)


matrix_row = []
n = int(input())
for i in range(n):
    row = []
    for x in range(1, n + 1):
        row.append(x)
    matrix.append(row)
[print(row) for row in matrix_row]