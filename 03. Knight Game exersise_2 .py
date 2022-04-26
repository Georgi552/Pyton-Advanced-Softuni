def is_knight_placed(board, row, col):

    if row < 0 or col < 0 or row >= len(board) or col >= len(board):
        return False
    else:
        return board[row][col] == "K"

def affected_knights(board, row, col):
    result = 0
    if is_knight_placed(board, row - 2, col - 1):
        result += 1
    if is_knight_placed(board, row - 2, col + 1):
        result += 1
    if is_knight_placed(board, row + 2, col - 1):
        result += 1
    if is_knight_placed(board, row + 2, col + 1):
        result += 1
    if is_knight_placed(board, row - 1, col - 2):
        result += 1
    if is_knight_placed(board, row - 1, col + 2):
        result += 1
    if is_knight_placed(board, row + 1, col - 2):
        result += 1
    if is_knight_placed(board, row + 1, col + 2):
        result += 1
    return result

n_rows = int(input())

matrix = []
for i in range(n_rows):
    row = [el for el in input()]
    matrix.append(row)


removed_knights = 0
counter = 0
while True:
    max_count = 0
    max_r = 0
    max_c = 0
    for r in range(n_rows):
        for c in range(n_rows):
            if matrix[r][c] == "0":
                continue

            count = affected_knights(matrix, r, c)
            if count > max_count:
                max_count = count
                max_r = r
                max_c = c

    if max_count == 0:
        break
    matrix[max_r][max_c] = "0"
    removed_knights += 1
    counter += 1

print(removed_knights)






