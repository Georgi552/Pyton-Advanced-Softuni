n, m = input().split(" ")


m_set = set()
set_n = set()

for i in range(int(n) + int(m)):
    if i < int(m):
        set_n.add(input())
    if i >= int(m):
        m_set.add(input())

for el in (set_n.intersection(m_set)):
    print(el)

