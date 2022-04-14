clothes = input().split(" ")
capacity = int(input())
clothes_on_rack = 0
number_racks = 1

for el in clothes:
    if (int(clothes_on_rack) + int(el)) < capacity:
        clothes_on_rack += int(el)

    elif (int(clothes_on_rack) + int(el)) == capacity:
        number_racks += 1
        clothes_on_rack = 0

    elif (int(clothes_on_rack) + int(el)) > capacity:
        number_racks += 1
        clothes_on_rack = int(el)

print(number_racks)