a = [int(i) for i in open('17var05.txt')]
res = []
for i in range(len(a)-1):
    if a[i] % 27 == min(a) or a[i+1] % 27 == min(a):
        res.append(a[i] + a[i+1])
print(len(res), max(res))