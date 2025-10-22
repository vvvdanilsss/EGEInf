a = [int(i) for i in open('txt/ex6.txt')]
minn = min(i for i in a)
res = []
for i in range(len(a) - 1):
    a1, a2 = a[i], a[i + 1]
    s = a1 + a2
    if (a1 % 65 == minn) and (a2 % 65 == minn):
        res.append(s)
print(len(res), max(res))
