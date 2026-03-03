def solve():
    # matrix[i][j] = длина дороги между (i+1) и (j+1), 0 если дороги нет
    matrix = [
        [0, 12, 17,  6,  0,  0, 10,  0],
        [12, 0,  0,  0,  0,  7,  0,  0],
        [17, 0,  0,  0, 16,  0,  0, 20],
        [6,  0,  0,  0,  4,  0,  8,  0],
        [0,  0, 16,  4,  0,  0,  0,  9],
        [0,  7,  0,  0,  0,  0, 11, 18],
        [10, 0,  0,  8,  0, 11,  0,  0],
        [0,  0, 20,  0,  9, 18,  0,  0],
    ]

    n = 8
    g = {i: set() for i in range(n)}
    w = {}
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                g[i].add(j)
                w[(i, j)] = matrix[i][j]

    deg = {i: len(g[i]) for i in range(n)}

    D = next(v for v in range(n) if deg[v] == 4)
    F = next(v for v in range(n) if deg[v] == 2)

    C = next(v for v in g[F] if v != D)

    # A — сосед C (кроме F), который соединён с D
    A = next(v for v in g[C] if v != F and D in g[v])

    # B — третий сосед A (кроме C и D)
    B = next(v for v in g[A] if v not in (C, D))

    # E — третий сосед B (кроме A и D)
    E = next(v for v in g[B] if v not in (A, D))

    ans = w[(A, D)] + w[(B, E)]
    print(ans)

solve()
