def M(n):
    s = []
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            if d != n // d:
                s.append(n // d)
                if len(s) == 2:
                    return sum(s)
    if len(s) == 1:
        return n // s[0] + s[0]
    return 0


d = []
for i in range(256123000, 256234001):
    if M(i) % 10000 == 1234:
        d.append([i, M(i)])
d.sort(key=lambda x: -x[1])
for row in d: print(*row)







