r = 999999
n = 1000

while r != 7434:
    n -= 1
    lst_n = [int(_) for _ in str(n)]
    a, b = lst_n[0]**2 + lst_n[1]**2, lst_n[1]**2 + lst_n[2]**2
    r = int(f"{a}{b}") if a > b else int(f"{b}{a}")

print(f"max_n = {n}, r = {r}")

