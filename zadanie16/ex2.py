def f(n):
    s = [0] * (n + 1)
    for i in range(1, (n + 1)):
        if i < 3:
            s[i] = 1
        elif (i > 2) and (i % 2 == 0):
            s[i] = s[i - 1] + i - 1
        elif (i > 2) and (i % 2 != 0):
            s[i] = s[i - 2] + 2 * i - 2
    return s[n]


print(f(3048) - f(3045))
