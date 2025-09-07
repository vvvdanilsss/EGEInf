counter: int = 0
n: int = 999

while n < 10000:
    n += 1
    s = str(n)
    if len(s) != len(set(s)):
        continue

    for i in range(len(s) - 1):
        if int(s[i]) % 2 == int(s[i + 1]) % 2:
            break
    else:
        counter += 1

print(counter)
