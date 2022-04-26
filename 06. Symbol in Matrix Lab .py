n_rows = int(input())

matrix = []
for i in range(n_rows):
    simb = input()
    row = []
    for el in simb:
        row.append(el)
    matrix.append(row)

searched_simb = input()
index_found = []
for r in range(n_rows):
    for c in range(n_rows):
        if matrix[r][c] == searched_simb:
            index_found.append(r)
            index_found.append(c)
            print(f"({r}, {c})")
        if len(index_found) > 0:
            break

if len(index_found) < 1:
    print(f"{searched_simb} does not occur in the matrix")