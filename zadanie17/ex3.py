def sum3(n):
    s = 0
    while n != 0:
        s += n % 3
        n //= 3
    return s


a = [int(i) for i in open('txt/3.txt')]
max11 = sum3(max(i for i in a if i % 11 == 0))
counter = 0
minp = 100000
for i in range(len(a) - 1):
    a1, a2 = sum3(a[i]), sum3(a[i + 1])
    if a1 == max11 or a2 == max11:
        counter += 1
        s = a[i] + a[i + 1]
        if s < minp:
            minp = s
print(counter, minp)
