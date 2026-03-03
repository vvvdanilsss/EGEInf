res = []
s = 0
max_s = 0
a = [str(i) for i in open('txt/24-263.txt')]
for i in range(0, len(a[0]) - 1):
    if a[0][i] != a[0][i+1]:
        s += 1
        if s > max_s:
            max_s = s
    else:
        s = 1
print(max_s)
