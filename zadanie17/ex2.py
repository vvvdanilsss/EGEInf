a = [int(i) for i in open('txt/17-354.txt')]
min3 = min(i for i in a if abs(i) % 10 == 3) ** 2
counter = 0
max2 = -1
for i in range(len(a) - 1):
    a1, a2 = a[i], a[i + 1]

    if (abs(a1) % 10 == 3) ^ (abs(a2) % 10 == 3):
        if a1 ** 2 + a2 ** 2 < min3:
            counter += 1
            if a1 ** 2 + a2 ** 2 > max2:
                max2 = a1 ** 2 + a2 ** 2
print(counter, max2)

