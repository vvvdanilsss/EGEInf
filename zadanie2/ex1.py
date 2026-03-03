print('w x y z f')
for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                F = not(y <= x) or (not(w) == (z <= y)) or z
                if F == False:
                    print(w, x, y, z, F)
