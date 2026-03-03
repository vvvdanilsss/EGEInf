from itertools import product

res = []
t = [1, 2, 3, 4, 5, 6]
T = list(product(t, repeat=4))
for i in T:
    if i.count(3) == 1:
        n = 0
        for j in i:
            if j % 2 != 0:
                n += 1
        if n >= 2:
            res.append(i)
print(len(res))



