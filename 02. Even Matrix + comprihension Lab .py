row_length =  int(input())

matrix = []
evan_matric = []
evans = []
for i in range(row_length):
    row = []
    for el in input().split(", "):
        if int(el) % 2 == 0:

            row.append(int(el))
    evan_matric.append(row)

print(evan_matric)

# rows = int(input())
#
# matrix = []
#
# for i in range(rows):
#     row = input().split(", ")
#     matrix.append(row)
#
# evens = [[int(x) for x in row if int(x) % 2 == 0] for row in matrix]
#
# print(evens)