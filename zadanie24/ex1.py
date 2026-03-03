with open('24var07.txt', 'r') as a:
    s = a.read()
r = '*-'
c = 0

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

# шаблон для корректного выражения:
# число без ведущих нулей (\d+), операция [+*-], числа повторяются
pattern = re.compile(r'(?:[1-9]\d*(?:[+\-*][1-9]\d*)*)')

# находим все совпадения
matches = pattern.findall(s)

# выбираем максимальное по длине
max_expr = max(matches, key=len)

print("Максимальное корректное выражение:", max_expr)
print("Количество символов:", len(max_expr))
