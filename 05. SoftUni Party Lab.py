n = int(input())
invited_gests = set()
arrived_gests = set()

for i in range(n):

    invited_gests.add(input())

arrived = input()
while not arrived == "END":
    if len(arrived) == 8:
        if arrived in invited_gests:
            arrived_gests.add(arrived)

    arrived = input()

not_arrived = invited_gests.difference(arrived_gests)
print(len(not_arrived))

vip_not_arrived = set()
reg_not_arrived = set()
for guest in not_arrived:
    if guest[0].isdigit():
        vip_not_arrived.add(guest)
    else:
        reg_not_arrived.add(guest)
print("\n".join(sorted(vip_not_arrived)))
print('\n'.join(sorted(reg_not_arrived)))
