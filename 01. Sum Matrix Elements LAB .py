rows_count, colums_count = [int(x) for x in input().split(", ")]
total_sum = 0
matrix = []
for i in range(rows_count):
    rom = [int(x) for x in input().split(", ")]
    matrix.append(rom)


for row in matrix:
    total_sum += sum(row)
print(total_sum)
print(matrix)