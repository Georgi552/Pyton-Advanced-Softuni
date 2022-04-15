text = input()
all_elements = {}
for el in text:
    if el not in all_elements:
        all_elements[el] = 1
    else:
        all_elements[el] += 1

for key, value in sorted(all_elements.items()):
    print(f"{key}: {value} time/s")