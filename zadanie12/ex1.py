def tr(s):
    while ('19' in s) or ('399' in s) or ('999' in s):
        i = s.find('19')  # '123451946752'
        if i != -1:
            s = s[:i] + '9' + s[i + 2:]
        i = s.find('399')  # '123451946752'
        if i != -1:
            s = s[:i] + '91' + s[i + 3:]
        i = s.find('999')  # '123451946752'
        if i != -1:
            s = s[:i] + '3' + s[i + 3:]
    return s


ans = 0
for n in range(4, 10_000):
    s0 = '1' + '9' * n
    s = tr(s0)
    sum_s = sum(map(int, s))
    if sum_s == 33:
        ans = n
        break
print(ans)
