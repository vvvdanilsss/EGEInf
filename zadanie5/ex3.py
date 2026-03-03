r = 0
N = 1
res = []
while r <= 416:
    n = bin(N)[2:]
    if N % 3 == 0:
        n += n[-3:]
        r = int(n, 2)
    else:
        n += bin(((N % 3) + 1) * 3)[2:]
    R = int(n, 2)
    N += 1
    if r <= 416:
        res.append(r)
print(max(res))

