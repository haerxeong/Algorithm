#기후동행카드
'''A, B, C = map(int, input().split())
charge = A * 1300 + B * 1100 + C * 500
print(min(charge, 65000, 62000 + C * 500) if C else min(charge, 62000))'''

#해시 함수
'''S = input()
ans = 0
num = ''
for i in range(len(S)):
    if ord('A') <= ord(S[i]) <= ord('Z'):
        ans += ord(S[i]) + 35
    elif ord('a') <= ord(S[i]) <= ord('z'):
        ans += ord(S[i]) + 103
    else:
        num += S[i]
        print(num)
        if i + 1 < len(S) and S[i + 1] != int(S[i + 1]):
            ans += int(num)
            num = ''
    if num: ans += int(num)
print(ans)'''
#
'''def isAtoZ(s):
    return ord('A') <= ord(s) <= ord('Z')
def isatoz(s):
    return ord('a') <= ord(s) <= ord('z')

S = input()
ans = 0
num = ''
for i in range(len(S)):
    if isAtoZ(S[i]):
        ans += ord(S[i]) + 35
    elif isatoz(S[i]):
        ans += ord(S[i]) + 103
    else:
        num += S[i]
        if i + 1 < len(S) and (isAtoZ(S[i + 1]) or isatoz(S[i + 1])):
            ans += int(num)
            num = ''
if num: ans += int(num)
print(ans % 100)'''

#한진이의 상품뽑기 #그리디
#M-1이 될 때까지 빼고 K가 0이면 더하기 1 << 안해서 틀린사람 많!
'''N, M, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(N):
    while 0 < A[i] < M:
        ans += 1
        A[i] -= 1
print(ans)'''

#곱빼기
'''import math

def isPower2(n):
    return n == 2**(int(math.log2(n)))

n = int(input())
ans = []

if isPower2(n):
    ans.append(int(math.log2(n)))

else:
    x = int(math.log2(n) + 1)
    ans.append(x)
    x = 2**x - n
    while x > 0:
        print(x)
        if isPower2(x):
            ans.append(int(math.log2(x)))
            break

        y = int(math.log2(x))
        ans.append(y)
        x -= 2**y
    
print(' '.join(map(str, ans)))'''

#캣타워 - 삼성 코테 빈출 유형
def rotate1(arr):
    ans = [[0] * N for _ in range(M)]
    for i in range(N):
        for j in range(M):
            ans[j][N - i - 1] = arr[i][j]

    for i in range(M - 2, -1, -1):
        for j in range(N):
            if ans[i + 1][j] == 0 and ans[i][j] == 1:
                for k in range(i, -1, -1):
                    ans[k + 1][j] = ans[k][j]
                ans[k][j] = 0
    return ans

def rotate_1(arr): #왼쪽회전
    ans = [[0] * N for _ in range(M)]
    for i in range(N):
        for j in range(M):
            ans[M - j - 1][i] = arr[i][j]

    for i in range(M - 2, -1, -1):
        for j in range(N):
            if ans[i + 1][j] == 0 and ans[i][j] == 1:
                for k in range(i, -1, -1):
                    ans[k + 1][j] = ans[k][j]
                ans[k][j] = 0
    return ans

def gravity(arr): #님아 2일때 중력 고려 안해서 틀림;;
    pass

N, M = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(N)]

Q = int(input())
for _ in range(Q):
    v = int(input())
    if v == 1:
        li = rotate1(li)
    else:
        li = rotate_1(li)
    N, M = M, N

for i in range(N):
    for j in range(M):
        print(li[i][j], end = ' ')
    print()

#저것도 먹을거란 말이야 
#그리디 - 크기가 3인 자료구조 -> 음식당 최대 3개만 저장 - food[taste] += min(k, 3)
#math - 음식이 가장 많은 맛의 음시 개수를 줄여가며 N개의 음식만 남김 - while n < food[0] + food[1] + food[2]:
'''N, M = map(int, input().split())
li = []
for _ in range(M):
    li.append(list(input().split()))
'''

#금괴를 찾아라 - 정렬 + dp?
N = int(input())
weights = list(map(int, input().split()))
DP = [weights[i] for i in range(N)]
for i in range(1, N):
    if DP[i - 1] < DP[i]:
        DP[i] += DP[i - 1]

for i in range(N - 1, 0, -1):
    if DP[i] < DP[i - 1]:
        DP[i - 1] += DP[i]

ans = max(DP)
print(DP.index(ans) + 1)
print(ans)

#차이를 최대로! - 우선순위큐 / 세그먼트 트리 / 모노톤 큐
'''
from collections import deque

N, k = map(int, input().split())
li = list(map(int, input().split()))
ans = []
right = k - 1
Q = deque()
for i in range(k):
    Q.append(li[i])
for left in range(N):
    ans.append(max(Q) - min(Q))
    right += 1
    if right == N: right = 0
    Q.popleft()
    Q.append(li[right])
print(' '.join(map(str, ans)))
'''
#
'''from collections import deque

N, k = map(int, input().split())
li = list(map(int, input().split()))
ans = []
right = k - 1
Q = deque()

for i in range(k):
    Q.append(li[i])
minVal, maxVal = min(Q), max(Q)

for left in range(N):
    ans.append(maxVal - minVal)

    right += 1
    if right == N: right = 0

    pop = Q.popleft()
    push = li[right]
    Q.append(push)

    if pop == minVal: minVal = min(Q)
    elif pop == maxVal: maxVal = max(Q)
    minVal = min(push, minVal)
    maxVal = max(push, maxVal)
print(' '.join(map(str, ans)))'''

#조상노드 - LCA, dfs
#모든 Q에 대해 매번 구할 수 없음 
'''N = int(input())
trees = [[] for _ in range(N + 1)] #부모 저장 리스트
for _ in range(N - 1):
    U, V = map(int, input().split()) #U가 V의 부모 - V가 자식
    trees[V].append(U)
    trees[V].extend(trees[U])

for _ in range(int(input())):
    A, B = map(int, input().split()) #A가 B의 조상인지
    print(int(A in trees[B]), end = ' ')
'''
'''def isParent(A, B):
    if not len(parents[B]): return False
    if parents[B] == A:
        return True
    else:
        return isParent(parents[B], B)

N = int(input())
parents = [0] * (N + 1) #부모 저장 리스트
for _ in range(N - 1):
    U, V = map(int, input().split()) #U가 V의 부모 - V가 자식
    parents[V] = U

for _ in range(int(input())):
    A, B = map(int, input().split()) #A가 B의 조상인지 - 배열[B]에 A가 있는지
    print(int(isParent(A, B)), end = ' ')
'''

import sys
sys.setrecursionlimit(10**5)

def isParent(A, B):
    if not parents[B]: return False
    if parents[B] == A:
        return True
    else:
        return isParent(A, parents[B])

N = int(input())
parents = [0] * (N + 1) #부모 저장 리스트
for _ in range(N - 1):
    U, V = map(int, input().split()) #U가 V의 부모 - V가 자식
    parents[V] = U

for _ in range(int(input())):
    A, B = map(int, input().split()) #A가 B의 조상인지 - 배열[B]에 A가 있는지
    print(int(isParent(A, B)), end = ' ')

#따릉이와 퀵보드 - Dijkstra, 플로이드 워셜
