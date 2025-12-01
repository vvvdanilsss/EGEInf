def f(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


r = []
for i in range(7521, 10 ** 9, 7521):
    s = str(i)
    if s[1:3] == '13' and s[-1] == '9' and '79' in s[3:-1]:
        r.append([i, f(i)])
r.sort(key=lambda x: (x[1], x[0]))
for row in r: print(*row)


import re


mask = re.compile(r'^[1-9]13\d*79\d*9$')
limit = 10 ** 9
step = 7521


def sumn(n):
    return sum(int(i) for i in str(n))


nums = []
n = step
while n <= limit:
    if mask.fullmatch(str(n)):
        nums.append([n, sumn(n)])
    n += step
nums.sort(key=lambda x: (x[1], x[0]))
print('___')
for row in nums: print(*row)

