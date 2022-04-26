def chess(row, col):

    if col == 0:
        col = 'a'
    if col == 1:
        col = 'b'
    if col == 2:
        col = 'c'
    if col == 3:
        col = 'd'
    if col == 4:
        col = 'e'
    if col == 5:
        col = 'f'
    if col == 6:
        col = 'g'
    if col == 7:
        col = 'h'

    if row == 0:
        row = 8
    elif row == 1:
        row = 7
    elif row == 2:
        row = 6
    elif row == 3:
        row = 5
    elif row == 4:
        row = 4
    elif row == 5:
        row = 3
    elif row == 6:
        row = 2
    elif row == 7:
        row = 1

    return row, col
print(chess(1,7))
