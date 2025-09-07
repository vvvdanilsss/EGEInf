def r(n: int) -> int:
    n_bin: str = bin(n)  # "0b01010100101"
    counter = 0
    for s in n_bin:
        if s == "1":
            counter += 1

    n_bin += str(counter % 2)
    return int(n_bin, 2)


n = 0
while r(r(n)) <= 253:
    n += 1

print(n)

