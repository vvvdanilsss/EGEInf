for x in range(1, 10000):
    n = 27 ** 7 - 3 ** 11 + 36 - x
    s = []
    while n > 0:
        s.append(n % 3)
        n //= 3
    if sum(s) == 22:
        print(x)
        break