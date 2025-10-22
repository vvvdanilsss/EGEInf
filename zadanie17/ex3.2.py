a = [int(i) for i in open('txt/17-354.txt')]
maxa = max(i for i in a if i % 11 == 0)
maxa3 = 0
c = 0
while maxa != 0:
    maxa3 += maxa % 3
    maxa //= 3
for i in range(len(a) - 1):
    a1, a2 = a[i], a[i + 1]

