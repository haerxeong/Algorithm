n = int(input())
F = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    if i == 1 or i == 2: F[i] = 1
    else: F[i] = F[i - 1] + F[i - 2]

print(F[n])