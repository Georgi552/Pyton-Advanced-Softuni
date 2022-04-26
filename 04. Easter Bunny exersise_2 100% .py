from sys import maxsize
def step_is_valid(matrica, row, col):
    if row < 0 or row >= len(matrica) or col < 0 or col >= len(matrica):
        return False
    else:
        return True



n_rows = int(input())
# matrix input
matrix = []
for i in range(n_rows):
    row = input().split(" ")
    matrix.append(row)

# buny Location
buny_row = []
buny_col = []
for r in range(0, len(matrix)):
    for c in range(0, len(matrix[r])):
        if matrix[r][c] == "B":
            buny_row = r
            buny_col = c
most_colected_egs = -maxsize
best_path = []
best_direction = []


current_direction = []
current_path = []
current_colected_egs = 0

# determin direction
for dire in range(4):

    step = 1
    current_colected_egs = 0
    current_path = []
    current_row = []
    current_col = []

    # moving up
    if dire == 0:
        current_direction = "up"
        while True:
            if step_is_valid(matrix, buny_row - step, buny_col) is False:
                break
            elif matrix[buny_row - step][buny_col] == "X":
                break
            elif step_is_valid(matrix, buny_row - step, buny_col) is True:
                path = [buny_row - step, buny_col]
                current_path.append(path)
                current_colected_egs += int(matrix[buny_row - step][buny_col])
                step += 1

    # moving down
    if dire == 1:
        current_direction = "down"
        while True:
            if step_is_valid(matrix, buny_row + step, buny_col) is False:
                break
            elif matrix[buny_row + step][buny_col] == "X":
                break
            elif step_is_valid(matrix, buny_row + step, buny_col) is True:
                path = [buny_row + step, buny_col]
                current_path.append(path)
                current_colected_egs += int(matrix[buny_row + step][buny_col])
                step += 1

    # moving left
    if dire == 2:
        current_direction = "left"
        while True:
            if step_is_valid(matrix, buny_row, buny_col - step) is False:
                break
            elif matrix[buny_row][buny_col - step] == "X":
                break
            elif step_is_valid(matrix, buny_row, buny_col - step) is True:
                path = [buny_row, buny_col - step]
                current_path.append(path)
                current_colected_egs += int(matrix[buny_row][buny_col - step])
                step += 1

    # moving right
    if dire == 3:
        current_direction = "right"
        while True:
            if step_is_valid(matrix, buny_row, buny_col + step) is False:
                break
            elif matrix[buny_row][buny_col + step] == "X":
                break
            elif step_is_valid(matrix, buny_row, buny_col + step) is True:
                path = [buny_row, buny_col + step]
                current_path.append(path)
                current_colected_egs += int(matrix[buny_row][buny_col + step])
                step += 1


    if current_colected_egs >= most_colected_egs:
        most_colected_egs = current_colected_egs
        best_path = current_path
        best_direction = current_direction


print(best_direction)
for i in range(len(best_path)):
    print(best_path[i])
print(most_colected_egs)