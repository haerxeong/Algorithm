#simulation

#15686번: 치킨 배달
'''from itertools import combinations as cb

n, m = map(int, input().split())
City = [list(map(int, input().split())) for _ in range(n)]
Home = []
Chicken = []
ans = []

for i in range(n):
    for j in range(n):
        if City[i][j] == 1: Home.append((i, j))
        if City[i][j] == 2: Chicken.append((i, j))

for ch in cb(Chicken, m):
    city_dist = 0
    for hx, hy in Home:
        home_dist = 1000
        for cx, cy in ch:
            home_dist = min(home_dist, abs(hx - cx) + abs(hy - cy))
        city_dist += home_dist
    ans.append(city_dist)

print(min(ans))'''

#11559번: Puyo Puyo
'''field = [list(input()) for _ in range(12)]
chain = 0
for i in range(12):
    for j in range(6):
        pass'''

#two pointer

#2467번: 용액
'''N = int(input())
li = list(map(int, input().split()))
left, right = 0, N - 1
minVal = abs(li[0] + li[N-1])
ans = [left, right]

while left != right:
    temp = li[left] + li[right]
    if minVal > abs(temp):
        minVal = abs(temp)
        ans = [left, right]

    if temp >= 0:
        right -= 1
    else:
        left += 1

print(li[ans[0]], li[ans[1]])'''

#2003번: 수들의 합 2
'''N, M = map(int, input().split())
A = list(map(int, input().split()))
i, j = 0, N
cnt = 0

for i in range(N):
    for j in range(i, N):
        if sum(A[i:j+1]) == M:
            cnt += 1
            break
        
print(cnt)'''

'''N, M = map(int, input().split())
A = list(map(int, input().split()))
i, j = 0, 0
cnt = 0

while i <= j and j < N:
    temp = sum(A[i:j+1])
    if temp == M:
        cnt += 1
        i += 1
        j = i
    elif temp > M:
        i += 1
        j = i
    else:
        j += 1
print(cnt)'''

#7795번: 먹을 것인가 먹힐 것인가
'''for _ in range(int(input())):
    cnt = 0

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    A_pointer, B_pointer = 0, 0
    
    while A_pointer < N:
        if A[A_pointer] > B[B_pointer]:
            cnt += 1

            if B_pointer + 1 < M:
                B_pointer += 1
            else:
                A_pointer += 1
                B_pointer = 0
            
        else:
            A_pointer += 1
            B_pointer = 0

    print(cnt)'''

'''for _ in range(int(input())):
    cnt = 0

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    A_pointer, B_pointer = 0, 0
    
    while A_pointer < N:
        while B_pointer < M and A[A_pointer] > B[B_pointer]:
            cnt += 1
            B_pointer += 1
        A_pointer += 1
        B_pointer = 0

    print(cnt)'''

'''for _ in range(int(input())):
    cnt = 0

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()
    B_pointer = 0

    for A_pointer in range(N):
        while B_pointer != M and A[A_pointer] > B[B_pointer]:
            B_pointer += 1
        cnt += B_pointer

    print(cnt)'''

#14465번: 소가 길을 건너간 이유 5
'''Defect = []
minNum = float('inf')

N, K, B = map(int, input().split())
for _ in range(B):
    Defect.append(int(input()))

for i in range(N - K):
    num = 0
    for j in range(i, i + K):
        if j in Defect:
            num += 1
    minNum = min(minNum, num)

print(minNum)'''

'''Defect = []
minNum = 0
tempNum = 0

N, K, B = map(int, input().split())
for _ in range(B):
    Defect.append(int(input()))

left, right = 1, K + 1

for i in range(1, K + 1):
    if i in Defect:
        minNum += 1
tempNum = minNum

while right < N + 1:
    if left in Defect and right not in Defect:
        tempNum -= 1
    elif left not in Defect and right in Defect:
        tempNum += 1
    minNum = min(minNum, tempNum)
    right += 1
    left += 1

print(minNum)'''

#1806번: 부분합
'''N, S = map(int, input().split())
li = list(map(int, input().split()))
li.sort() #연속된 수들의 부분합임... 정렬 ㄴ
ans = 0

left, right = N - 1, N

while left > 0:
    temp = sum(li[left:right])
    if temp >= S:
        ans = right - left 
        break
    else:
        left -= 1

print(ans)'''

'''N, S = map(int, input().split())
li = list(map(int, input().split()))
minLen = float('inf')
partSum = li[0]

if sum(li) < S:
    print(0)
else:
    left, right = 0, 0
    while left <= right < N:
        if partSum >= S:
            minLen = min(minLen, right - left + 1)
            partSum -= li[left]
            left += 1
        else:
            if right + 1 < N: partSum += li[right + 1]
            right += 1

    print(minLen)'''
    
#test
#1966번: 프린터 큐 
'''from collections import deque

for _ in range(int(input())):
    cnt = 1
    N, M = map(int, input().split())
    Q = deque(map(int, input().split()))
    
    while Q:
        front = Q.popleft()
        if max(Q) == front:
            N -= 1
            M -= 1
            cnt += 1

        else:
            Q.append(front)

            if M == 0:
                M = N - 1
            else:
                M -= 1

    print(cnt)
                '''
'''
from collections import deque

for _ in range(int(input())):
    cnt = 0
    N, M = map(int, input().split())
    Q = deque(map(int, input().split()))
    
    while Q:
        front = Q.popleft()
        M -= 1

        if max(Q) == front:
            cnt += 1
            if M < 0:
                break

        else:
            Q.append(front)

            if M < 0:
                M = len(Q) - 1

    print(cnt)
                ''' #왜1!!!!!

#2230번: 수 고르기
'''N, M = map(int, input().split())
A = sorted([int(input()) for _ in range(N)])
minVal = float('inf')

left, right = 0, 0

while left <= right < N: #원래 left 조건은 안 넣었는데 반례로 1 0 1넣으니까 에러! 떠서 수정함~
    diff = A[right] - A[left]
    if diff >= M: #조건 충족
        minVal = min(minVal, diff)
        left += 1
    else: #차이가 M보다 작을 경우
        right += 1

print(minVal)
'''
