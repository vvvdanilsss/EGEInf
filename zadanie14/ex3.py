def f(n):
    res = ''
    while n:
        res += str(n % 6)
        n = n // 6
        return res[::-1]


for x in range(1001):
    if f(x)[-2:] == '00':
        print(x, f(x))
        break
