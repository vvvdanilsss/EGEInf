def R(n: int) -> int:
    n_bin = counter(bin(n))
    r_bin = counter(n_bin)
    r = int(r_bin, 2)
    return r


def counter(n_bin: str) -> str:
    counter = n_bin.count('1')
    last_number = str(counter % 2)
    n_bin += last_number
    return n_bin


N = 1
while R(N) <= 253:
    N += 1

print(N)
