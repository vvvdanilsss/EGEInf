a = [int(i) for i in open('ex8.txt')]
min2 = min(i for i in a if abs(i) % 10 == 1) ** 2
res = []
for i in range(len(a) - 1):
    a1, a2 = a[i], a[i + 1]
    s2 = (a1 ** 2) + (a2 ** 2)
    s = a1 + a2
    if ((abs(a1) % 10) == (abs(a2) % 10)) and ((abs(a1) % 3 == 0) ^ (abs(a2) % 3 == 0)) and (s2 <= min2):
        res.append(s)
print(len(res), max(res))

