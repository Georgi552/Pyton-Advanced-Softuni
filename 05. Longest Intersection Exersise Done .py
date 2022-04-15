n = int(input())
longest_intersection = set()
for i in range(n):
    first, second = input().split("-")  # 0,10-2,5
    first_start, first_end = [int(x) for x in first.split(",")]
    second_start, second_end = [int(x) for x in second.split(",")]
    first_range = set(range(first_start, first_end + 1))
    second_range = set(range(second_start, second_end + 1))
    intersection = second_range.intersection(first_range)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is [{', '.join([str(x) for x in longest_intersection])}] with length {len(longest_intersection)}")
