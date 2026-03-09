with open('24var07.txt', 'r') as a:
    s = a.read()
r = '*-'

sdf = []
counter = 0

for i in range(len(s) - 1):
    if s[i].isdigit():
        if counter == 0:
            if s[i] != '0':
                counter += 1
            else:
                counter = 0
            continue
        else:
            counter += 1

    elif counter != 0:
        if s[i + 1] not in r and s[i + 1] != '0':
            counter += 1
            continue
        else:
            sdf.append(counter)
            counter = 0

print(max(sdf))

import re

pattern = re.compile(r'[1-9]\d*(?:[\-*][1-9]\d*)*')

# finditer удобнее, если нужны позиции, но оставим findall
matches = pattern.findall(s)

if matches:
    max_expr = max(matches, key=len)
    print(f"Нашлось выражений: {len(matches)}")
    print(f"Максимальное: {max_expr}")
    print(f"Длина: {len(max_expr)}")
else:
    print("Ничего не найдено")