#stack, queue, dequeue, priority queue

#1874번: 스택 수열
'''n = int(input())
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
print(stack)'''

#1417번: 국회의원 선거


#큐
#

#덱
#2164번: 카드2
'''from collections import deque

N = int(input())
dq = deque(i for i in range(1, N + 1))

while len(dq) != 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq[0])'''

#8892번: 팰린드롬
for _ in range(int(input())):
    k = int(input())
    flag = False
    li = list(input() for _ in range(k))
    
    for i in range(k - 1):
        for j in range(i + 1, k):
            if li[i] + li[j] == (li[i] + li[j])[::-1]:
                print(li[i] + li[j])
                flag = True
                break
            if li[j] + li[i] == (li[j] + li[i])[::-1]:
                print(li[j] + li[i])
                flag = True
                break
        if flag: break
    if not flag: print(0)