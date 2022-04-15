n = int(input())
el = []
elements = set()

for i in range(n):
    raw_element = input().split(" ")
    for i in range(len(raw_element)):
        el.append(raw_element[i])
el_set = set(el)

for element in el_set:
    print(element)