# def f(n):
#     d = bin(n)[2:]
#     return str(d)
#
#
# res = []
# r = 68
# N = 12
# #for N in range(100000000):
# fa = int(f(N) + f(N)[-2:], 2) if N % 4 == 0 else int(f((N % 4) * 2) + f(N), 2)
# if fa < r:
#     res.append(N)
# N += 1
# print(max(res))

res = []
r = 0
N = 12
n = 0
while r < 68:
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