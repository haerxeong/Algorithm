input = __import__('sys').stdin.readline

N = int(input())
A = list(map(int, input().split()))
prefix = [0] * N

for i in range(N):
    prefix[i] += prefix[i - 1] + A[i]

for _ in range(int(input())):
    i, j = map(int, input().split())
    if i - 2 < 0: print(prefix[j - 1])
    else: print(prefix[j - 1] - prefix[i - 2])