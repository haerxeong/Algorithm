S = input().strip()
N = len(S)
max_len = 0

for length in range(2, N + 1, 2):  # 짝수 길이만
    for i in range(N - length + 1):
        sub = S[i:i + length]
        mid = length // 2
        left = sum(map(int, sub[:mid]))
        right = sum(map(int, sub[mid:]))
        if left == right:
            max_len = max(max_len, length)

print(max_len)