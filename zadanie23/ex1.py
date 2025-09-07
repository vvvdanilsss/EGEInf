def ways(start, end, ban=8):
    lst = [0] * (end + 1)
    lst[start] = 1
    for n in range(start + 1, end + 1):
        if n == ban:
            continue
        lst[n] += lst[n - 1]
        if n - 2 >= start:
            lst[n] += lst[n - 2]
        if n % 2 == 0 and n // 2 >= start:
            lst[n] += lst[n // 2]
    return lst[end]


print(ways(3, 14) * ways(14, 18))
