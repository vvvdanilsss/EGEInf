res = []
for n in range(1000):
    r = bin(n)[2:]
    if len(r) % 2 == 0:
        k = len(r) // 2
        r = r[:k] + '1' + r[k:]
    if int(r, 2) <= 26:
        res.append(int(r, 2))

print(max(res))
