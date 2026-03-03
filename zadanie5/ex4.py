res = []
r = 0
N = 1
n = 0
while r <= 545:
    if N % 4 == 0:
        n = bin(N)[2::]
        n += n[::]
        r = int(n, 2)
    else:
        n = bin(N)[2::]
        n += n[::-1]
        r = int(n, 2)
    res.append(N)
    N += 1
print(max(res))