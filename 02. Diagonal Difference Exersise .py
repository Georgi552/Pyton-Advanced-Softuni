n_rows = int(input())

matrix = []
for i in range(n_rows):
    matrix.append([int(x) for x in input().split(" ")])

primary_diagonal = []
secondary_diagonal = []

for i in range(n_rows):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][n_rows - 1 - i])
difference = sum(primary_diagonal) - sum(secondary_diagonal)
print(abs(difference))