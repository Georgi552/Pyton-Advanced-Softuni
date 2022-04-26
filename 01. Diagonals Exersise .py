n_rows = int(input())

matrix = []
for i in range(n_rows):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)


primary_diagonal = []
secondary_diagonal = []

for i in range(n_rows):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][n_rows - 1 - i])

print(f"Primary diagonal: {', '.join(map(str,primary_diagonal))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(map(str,secondary_diagonal))}. Sum: {sum(secondary_diagonal)}")