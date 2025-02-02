N, M = map(int, input().split())
alias = [list(input().split()) for _ in range(N)]
powers = [int(input()) for _ in range(M)]

for i in range(N):
    alias[i][1] = int(alias[i][1])

results = []

for power in powers:
    left, right = 0, N - 1
    while left <= right:
        mid = (left + right) // 2

        if alias[mid][1] >= power:
            right = mid - 1
        else:
            left = mid + 1

    results.append(alias[left][0])

print("\n".join(results))