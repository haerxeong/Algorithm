#15665번: N과 M (11)
# 백트래킹
def go(arr):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    for i in li:
        arr.append(i)
        go(arr)
        arr.pop()

N, M = map(int, input().split())
li = sorted(set(map(int, input().split())))
go([])

#1439번: 뒤집기
S = input()
li = [0, 0]
for i in range(len(S) - 1):
    if S[i + 1] != S[i]:
        li[int(S[i])] += 1
li[int(S[-1])] += 1

print(min(li))

#20301번: 반전 요세푸스
# N, K, M = map(int, input().split())