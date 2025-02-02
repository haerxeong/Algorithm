# 입력 처리
S = input()
queries = [input().split() for _ in range(int(input()))]

# 문자열 길이
n = len(S)

# 누적 합 배열 생성 (26개의 알파벳)
prefix = [[0] * n for _ in range(26)]

# 누적 합 계산
for i in range(n):
    char_index = ord(S[i]) - ord('a')  # 현재 문자에 해당하는 인덱스
    for j in range(26):
        prefix[j][i] = prefix[j][i - 1] if i > 0 else 0
    prefix[char_index][i] += 1

# 쿼리 처리 및 출력
results = []
for alpha, l, r in queries:
    l, r = int(l), int(r)
    char_index = ord(alpha) - ord('a')
    if l == 0:
        results.append(prefix[char_index][r])
    else:
        results.append(prefix[char_index][r] - prefix[char_index][l - 1])

# 결과 출력
print("\n".join(map(str, results)))