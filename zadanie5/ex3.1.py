r = 0
maxr = 0
N = 4
n = bin(N)[2:]
if N % 3 == 0:
    n += n[-3:]
else:
    n += bin(((N % 3) + 1) * 3)[2:]
r = int(n, 2)
print(r)
