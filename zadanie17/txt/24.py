s = open('24-263.txt').readline()

best = 0
cur = 0
prev = ''

for i in s:
    if i != prev:
        cur += 1
    else:
        cur = 1
    prev = i
    if cur > best:
        best = cur

print(best)