N = int(input())
sanguens = sorted(list(map(int, input().split())))
M = int(input())
cards = list(map(int, input().split()))
ans = [0] * M

for i in range(M):
    left, right = 0, N
    # upper bound: 처음으로 cards[i] 초과하는 위치
    while left < right:
        mid = (left + right) // 2
        if sanguens[mid] > cards[i]:
            right = mid
        else:
            left = mid + 1
    upper = left

    left, right = 0, N
    # lower bound: 처음으로 cards[i] 이상인 위치
    while left < right:
        mid = (left + right) // 2
        if sanguens[mid] >= cards[i]:
            right = mid
        else:
            left = mid + 1
    lower = left

    ans[i] = upper - lower

print(*ans)