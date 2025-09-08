def sum_r(n: int) -> int:
    s = 0
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            s += d
            if d != n // d:
                s += n // d
    return s


counter = 0
n = 500_001
while counter < 5:
    r = sum_r(n)
    if r % 10 == 6:
        counter += 1
        print(n, r)
    n += 1

