a = [int(i) for i in open('17-339.txt')]
mina = min(i for i in a if (i > 0) and (i % 19 == 0))
counter = 0
maxznach = -1000000
for i in range(len(a) - 1):
    a1 = a[i]
    a2 = a[i + 1]
    s = a1 + a2
    if s < mina:
        counter += 1
        if s > maxznach:
            maxznach = s
print(counter, abs(maxznach))
