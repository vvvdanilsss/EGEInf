a = [int(i) for i in open('txt/ex5.txt')]
minn = min(i for i in a)
res = []
for i in range(len(a) - 1):
    a1, a2 = a[i], a[i + 1]
    s = a1 + a2
    if (a1 % 55 == minn) or (a2 % 55 == minn):
        res.append(s)
print(len(res), min(res))

