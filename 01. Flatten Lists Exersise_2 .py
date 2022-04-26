lists = input().split("|")
final_list = []
for i in range(len(lists) - 1, -1, -1):
    el = lists[i].split(' ')
    for i in el:
        if i.lstrip("-").isdigit():
            final_list.append(i)
print(f"{' '.join(final_list)}")