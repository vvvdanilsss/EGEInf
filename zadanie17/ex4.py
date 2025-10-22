def f(n):
    if (10000 > abs(n) > 999) and (abs(n) % 10 == 6):
        return True
    else:
        return False


res = []
a = [int(i) for i in open('txt/ex4.txt')]
minp = min(i for i in a if (i > 0) and f(i))
for i in range(len(a) - 2):
    a1, a2, a3 = a[i], a[i + 1], a[i + 2]
    s = a1 + a2 + a3
    if (f(a1) + f(a2) + f(a3)) == 1 and (s <= minp):
        res.append(s)
print(len(res), max(res))



