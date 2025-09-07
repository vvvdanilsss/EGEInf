def F(n):
    if n >= 2025:
        return n
    if n < 2025:
        return n * 2 + F(n + 2)


print(F(82) - F(81))
