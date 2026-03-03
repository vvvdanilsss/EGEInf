lst = list(map(str, input().lower().split()))
d = {i: lst.count(i) for i in lst}
if 'и' in d:
    print(d['и'])
else:
    print(0)
