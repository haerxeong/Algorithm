N = int(input())
M = int(input())
li = sorted(list(map(int, input().split())))
left, right = 0, N - 1
cnt = 0

while left != right:
    if li[left] + li[right] == M:
        cnt += 1
        left += 1
    elif li[left] + li[right] < M:
        left += 1
    else:
        right -= 1

print(cnt)