from math import factorial
def F(n):
    f = [0] * (n + 1)
    for i in range(1, (n + 1)):
        if i == 1:
            f[i] = 1
        elif i > 1:
            f[i] = (i - 1) * f[i - 1]
    return f[n]


print((factorial(2023) + 2 * factorial(2022)) / factorial(2021))

print(F(10), factorial(9))