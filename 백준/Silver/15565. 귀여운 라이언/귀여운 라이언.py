input = __import__('sys').stdin.readline

N, K = map(int, input().split())
dolls = list(map(int, input().split()))

left = 0
count = 0
min_len = float('inf')

for right in range(N):
    if dolls[right] == 1:
        count += 1

    while count >= K:
        min_len = min(min_len, right - left + 1)
        if dolls[left] == 1:
            count -= 1
        left += 1

print(min_len if min_len != float('inf') else -1)