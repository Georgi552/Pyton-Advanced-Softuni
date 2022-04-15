number = ([float(el) for el in input().split()])

result = {}
for num in number:
    if num not in result:
        result[num] = 0
    result[num] += 1

for key, value in result.items():
    print(f"{key} - {value} times")

#[print(f"{key} - {value} times") for key, value in result.items()]
