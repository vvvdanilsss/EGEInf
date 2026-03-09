def f_12(n):
    s = str(n)
    return int(s[0]) ** 2 + int(s[1]) ** 2


def f_23(n):
    s = str(n)
    return int(s[1]) ** 2 + int(s[2]) ** 2


for i in range(999, 99, -1):
    res = []
    if f_12(i) > f_23(i):
        res.append(f_12(i))
        res.append(f_23(i))
    else:
        res.append(f_23(i))
        res.append(f_12(i))
    if f'{res[0]}{res[1]}' == '7434':
        print(i)
