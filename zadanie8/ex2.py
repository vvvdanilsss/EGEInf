counter = 0
for n in range(1000, 10000):
    n_str = str(n)
    for s in n_str:
        if n_str.count(s) != 1:
            break
    else:
        for i in range(len(n_str) - 1):
            if int(n_str[i]) % 2 == int(n_str[i + 1]) % 2:
                break
        else:
            counter += 1

print(counter)


