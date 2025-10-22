a = [int(i) for i in open('txt/ex7.txt')]
min2 = min(i for i in a if abs(i) % 100 == 68) ** 2
res = []
for i in range(len(a) - 1):
    a1, a2 = a[i], a[i + 1]
    s2 = (a1 ** 2) + (a2 ** 2)
    if ((abs(a1) % 100 == 68) ^ (abs(a2) % 100 == 68)) and (s2 >= min2):
        res.append(s2)
print(len(res), max(res))