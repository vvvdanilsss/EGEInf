print('w x y z')
for w in 0, 1:
    for x in 0, 1:
        for y in 0, 1:
            for z in 0, 1:
                F = (z <= (not (y))) and ((not (x)) or y) and w
                if F == True:
                    print(w, x, y, z,)
