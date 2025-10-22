a = [int(i) for i in open('txt/17-354.txt')]
mina = min(i for i in a if abs(i) % 10 == 3) ** 2
c = 0
ms = -100000
m = []
for i in range(len(a) - 1):
    a1, a2 = a[i], a[i + 1]
    s = a1 ** 2 + a2 ** 2
    if (abs(a1) % 10 == 3) ^ (abs(a2) % 10 == 3):
        if s < mina:
            m.append(s)
            c += 1
print(c, max(m))