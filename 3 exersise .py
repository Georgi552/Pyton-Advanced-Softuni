
food_amount = int(input())
orders = input().split(" ")
max_order = 0
orders_done = []
orders_left = []
for el in orders:
    if int(el) > 0:
        if int(el) > int(max_order):
            max_order = el

for order in orders:
    if food_amount >= int(order):
        food_amount -= int(order)
        orders_done.append(order)
    else:
        break

for el in orders:
    if el not in orders_done:
        orders_left.append(el)


print(max_order)

if len(orders_left) == 0:
    print(f"Orders complete")
else:
    print(f"Orders left: {' '.join(orders_left)}")
