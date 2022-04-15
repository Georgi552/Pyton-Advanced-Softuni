n = int(input())
odd_values = set()
evan_values = set()

for i in range(1, n + 1):
    name = input()
    name_sum = sum([ord(el) for el in name]) // i
    if not (name_sum) % 2 == 0:
        odd_values.add((name_sum))
    else:
        evan_values.add((name_sum))

    evan_sum = sum(evan_values)
    odd_sum = sum(odd_values)

if evan_sum == odd_sum:
    result = odd_values.union(evan_values)

if evan_sum < odd_sum:
    result = odd_values.difference(evan_values)


if evan_sum > odd_sum:
    result = odd_values.symmetric_difference(evan_values)
print(', '.join([str(x) for x in result]))