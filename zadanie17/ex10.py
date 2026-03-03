def f(n):
    return n % 44


res = []
a = [int(i) for i in open('17var07.txt')]
for i in range(len(a)-1):
    if f(a[i]) + f(a[i+1]) == min(a):
        res.append(abs(a[i] - a[i+1]))
print(len(res), min(res))