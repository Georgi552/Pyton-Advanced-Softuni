n_rows, n_colums = input().split(" ")
n_rows, n_colums = int(n_rows), int(n_colums)

matrix = []
row = []
for r in range(0, n_rows):
    row = []
    el = []
    for c in range(0, n_colums):
        el = ''

        el = chr(97 + r) + chr(97 + r + c) + chr(97 + r)

        row.append(el)
    print(f"{' '.join(row)}")
    matrix.append(row)

