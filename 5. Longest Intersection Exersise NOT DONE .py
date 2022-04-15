n = int(input())
all_intersections = {}
first_set = set()
second_set = set()
for el in range(n):
    data = input().split("-")
    first = data[0].split(",")
    second = data[1].split(",")

    first_start = first[0]
    first_end = first[1]

    second_start = second[0]
    second_end = second[1]

    for fir in range(int(first_start), (int(first_end) + 1)):
        first_set.add(fir)


    fir = 0

    for sek in range(int(second_start), (int(second_end) + 1)):
        second_set.add(sek)


    sek = 0
    intersection = len(first_set.intersection(second_set))

    all_intersections[intersection] = (first_set.intersection(second_set))


    first_set.clear()
    second_set.clear()


longest_key = 0
longest_intersection = {}
for k, v in all_intersections.items():
    if k > longest_key:
        longest_intersection.clear()
        longest_intersection[k] = v
        longest_key = k


print(f"Longest intersection is [{' '.join(str(v) for v in longest_intersection.values())}] with length {' '.join(str(k) for k in longest_intersection.keys())}")


