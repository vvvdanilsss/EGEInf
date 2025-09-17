def F(n):
    f = [0] * (n + 1)
    for i in range(1, (n + 1)):
        if i == 1:
            f[i] = 1
        elif i > 1:
            f[i] = (i - 1) * f[i - 1]
    return f[n]


print((F(2024) + 2 * F(2023)) / F(2022))
