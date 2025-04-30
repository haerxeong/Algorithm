S = input()
ans = [-1] * 26

for i in range(len(S)):
    if ans[int(ord(S[i]) - ord('a'))] == -1: ans[int(ord(S[i]) - ord('a'))] = i

print(' '.join(map(str, ans)))