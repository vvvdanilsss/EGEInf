def D(v):
    if v < 2:
        return False
    if v == 2:
        return True
    if v % 2 == 0:
        return False
    d = 3
    while d ** 2 <= v:
        if v % d == 0:
            return False
        d += 2
    return True

def M(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0 and D(d) and str(d).count('5') == 1:
            nd = n // d
            if D(nd) and str(nd).count('5') == 1:
                return nd
    return 0


d = []
i = 1324728
while len(d) < 5:
    k = M(i)
    if k:
        d.append([i, k])
    i += 1
print(*d, sep='\n')
