S = input()
substrings = set()

# 모든 부분 문자열을 set에 추가
for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        substrings.add(S[i:j])

# 서로 다른 부분 문자열 개수 출력
print(len(substrings))