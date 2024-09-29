from itertools import permutations as pm

N = int(input())
A = list(map(int, input().split()))
max_value = 0

for i in pm(A, N):
    temp = 0
    for j in range(N - 1):
        temp += abs(i[j] - i[j + 1] )
    max_value = max(max_value, temp)

print(max_value)