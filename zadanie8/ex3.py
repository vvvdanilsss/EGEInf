from itertools import product
a = 0
t = ['А', 'Е', 'Л', 'Р', 'С', 'Т']
T = list(product(t, repeat=5))
for i, d in enumerate(T, start=1):
    d = ''.join(d)
    if i % 2 == 0 and d[0] != 'А' and d[0] != 'С' and d[0] != 'Т':
        k = 0
        if d.count('Л') == 2 and 'ЛЛ' not in d:
           a = i

print(a)
print(T)