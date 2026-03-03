def f(n):
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        if i == 1:
            s[i] = 1
        elif i > 1:
            s[i] = i + s[i - 1]
    return int(s[n])


print(f(3000) - f(2000))

print(sum(range(1, 3001)) - sum(range(1, 2001)))


