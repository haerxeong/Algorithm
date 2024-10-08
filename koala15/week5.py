#stack, queue, dequeue, priority queue

#1874번: 스택 수열
n = int(input())
li = [int(input()) for _ in range(n)]
stack, ans = [], []
current = 1
while current <= n + 1:
    if not stack or stack[-1] != li[0]:
        ans.append('+')
        stack.append(current)
        current += 1
    else:
        ans.append('-')
        stack.pop()
        li.pop(0)
    print(stack)
print('NO' if stack else '\n'.join(ans))
print(stack)

#17298번: 오큰수
N = int(input())
A = list(map(int, input().split()))
stack = [A[-1]]
ans = [-1]

for i in range(N - 2, -1, -1):
    while stack:
        if A[i] < stack[-1]:
            ans.append(stack[-1])
            
            break
        else: stack.pop()
    else:
        ans.append(-1)
    stack.append(A[i])

print(' '.join(map(str, ans[::-1])))

#큐
#1158번: 요세푸스 문제
from collections import deque
N, K = map(int, input().split())
cnt = 0
ans = []

Q = deque([i for i in range(1, N + 1)])
while Q:
    if cnt == K - 1:
        ans.append(Q.popleft())
    else: Q.append(Q.popleft())
    cnt = (cnt + 1) % K

print(f"<{', '.join(map(str, ans))}>")

#덱
#2164번: 카드2
from collections import deque

N = int(input())
dq = deque(i for i in range(1, N + 1))

while len(dq) != 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq[0])

#1021번: 회전하는 큐
from collections import deque

N, M = map(int, input().split())
target = deque(map(int, input().split()))
Deq = deque(i for i in range(1, N + 1))
cnt = 0

while target:
    if target[0] == Deq[0]:
        Deq.popleft()
        target.popleft()
    else:
        if Deq.index(target[0]) <= len(Deq) // 2:
            Deq.append(Deq.popleft())
        else:
            Deq.appendleft(Deq.pop())
        cnt += 1
print(cnt)

#우선순위 큐
#1927번: 최소 힙
input = __import__('sys').stdin.readline
from heapq import heappush, heappop
hq = []

for i in range(int(input())):
    x = int(input())
    if x:
        heappush(hq, x)
    else:
        print(0 if not hq else heappop(hq))

#11279번: 최대 힙
input = __import__('sys').stdin.readline
from heapq import heappush, heappop

hq = []
for _ in range(int(input())):
    x = int(input())
    if x:
        heappush(hq, -x) #이게되네
    else:
        print(0 if not hq else -heappop(hq))

#11286번: 절댓값 힙
input = __import__('sys').stdin.readline
from heapq import heappush, heappop

hq = []
for _ in range(int(input())):
    x = int(input())
    if x:
        heappush(hq, [abs(x), x])
    else:
        print(0 if not hq else heappop(hq)[1])

#1417번: 국회의원 선거
N = int(input())
me = int(input())
others = sorted([int(input()) for _ in range(N - 1)])
ans = 0

while others and me <= others[-1]:
    me += 1
    others[-1] -= 1
    ans += 1
    others.sort()
    
print(ans)
#우선순위 큐로 다시
from heapq import heapify, heappop, heappush

N = int(input())
me = int(input())
others = [-int(input()) for _ in range(N - 1)]
heapify(others) #반환값 없음
ans = 0

while others and me <= -others[0]:
    root = heappop(others) + 1
    me += 1
    ans += 1
    heappush(others, root)

print(ans)