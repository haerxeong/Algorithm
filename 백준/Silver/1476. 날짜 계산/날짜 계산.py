E, S, M = map(int, input().split())
e, s, m = 1, 1, 1
year = 1

while E != e or S != s or M != m:
    e += 1
    s += 1
    m += 1
    year += 1

    if e == 16: e = 1
    if s == 29: s = 1
    if m == 20: m = 1

print(year)
