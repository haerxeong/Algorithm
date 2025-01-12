L = int(input())  # S의 길이
S = sorted(list(map(int, input().split())))
n = int(input())  # n을 포함하면서 S의 요소는 포함되지 않음 -> 좋은 구간

# n이 집합 S에 이미 포함되어 있으면 좋은 구간이 없다.
if n in S:
    print(0)
    exit()

# n보다 작은 가장 큰 수와 n보다 큰 가장 작은 수 찾기
left = 0
right = S[0]

for s in S:
    if s < n:
        left = s
    elif s > n:
        right = s
        break

# 좋은 구간의 경우의 수 계산
ans = (n - left - 1) * (right - n) + (right - n - 1)
print(ans)