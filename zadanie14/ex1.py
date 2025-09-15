n = 15 * 240 ** 1500 - 10 * 343 ** 1200 + 40 * 49 ** 1000 - 35 * 7 ** 850 - 4805
s = []
counter = 0
while n > 0:
    s.append(n % 49)
    n //= 49
for i in s[::-1]:
    if i > 9:
        counter += 1
print(counter)
