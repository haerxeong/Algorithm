#10845: 큐
'''from collections import deque
input = __import__('sys').stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    command = list(input().split())
    if command[0] == 'push': q.append(command[1])
    elif command[0] == 'pop': print(q.popleft() if q else -1)
    elif command[0] == 'size': print(len(q))
    elif command[0] == 'empty': print(0 if q else 1)
    elif command[0] == 'front': print(q[0] if q else -1)
    else: print(q[-1] if q else -1)'''

#1966: 프린터 큐
'''from collections import deque
for _ in range(int(input())):
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))
    cnt = 0
    while q:
        maxq = max(q)
        front = q.popleft()
        m -= 1

        if maxq == front:
            cnt += 1
            if m < 0: print(cnt); break
        else: 
            q.append(front)
            if m < 0: 
                m = len(q) - 1''' #구글링
  
#10866: 덱
'''input = __import__('sys').stdin.readline
from collections import deque
dq = deque()

for _ in range(int(input())):
    command = list(input().strip().split())
    if command[0] == 'push_front': dq.appendleft(command[1])
    elif command[0] == 'push_back': dq.append(command[1])
    elif command[0] == 'pop_front': print(dq.popleft() if dq else -1)
    elif command[0] == 'pop_back': print(dq.pop() if dq else -1)
    elif command[0] == 'size': print(len(dq))
    elif command[0] == 'empty': print(0 if dq else 1)
    elif command[0] == 'front': print(dq[0] if dq else -1)
    else: print(dq[-1] if dq else -1)'''

#1942: 디지털시계
'''for i in range(3):
    a, b = input().split()
    h1, m1, s1 = map(int, a.split(':'))
    h2, m2, s2 = map(int, b.split(':'))
    cnt = 0
    while True:
        if s1 == 60: m1 += 1; s1 = 0
        if m1 == 60: h1 += 1; m1 = 0
        if h1 == 24: h1 = 0

        x = h1 * 10000 + m1 * 100 + s1
        if x % 3 == 0: cnt += 1

        if (h1 == h2) and (m1 == m2) and (s1 == s2): break
        s1 += 1
    print(cnt)'''

#2530: 인공지능 시계
'''h, m, s = map(int, input().split())
d = int(input())

d += (h * 3600 + m * 60 + s)
d %= 86400

h = d // 3600; d %= 3600
m = d // 60
s = d % 60

print(h, m, s)'''

#2525: 오븐 시계
'''a, b = map(int, input().split())
c = int(input())
c = (a * 60 + b + c) % (60 * 24)
a = c // 60
b = c % 60
print(a, b)'''

#3029: 경고 / #1408:24 ////////
'''h1, m1, s1 = map(int, input().split(":"))
h2, m2, s2 = map(int, input().split(":"))

if h1 == h2 and m1 == m2 and s1 == s2: print("24:00:00")
else:
    if s1 > s2: s2 += 60; m2 -= 1
    s = s2 - s1
    if m1 > m2: m2 += 60; h2 -= 1
    m = m2 - m1
    if h1 > h2: h2 += 24
    h = h2 - h1
    print("%02d:%02d:%02d" % (h, m, s))'''

#2852: NBA 농구 ///////////
'''n = int(input())
score = [0, 0]
ans = [0, 0]
before = 0
for _ in range(n):
    team, time = input().split()
    m, s = map(int, time.split(":")); team = int(team)
    time = m * 60 + s

    if score[0] > score[1]: ans[0] += time - before
    elif score[0] < score[1]: ans[1] += time - before

    before = time
    score[team - 1] += 1

if score[0] > score[1]: ans[0] += 48 * 60 - before
elif score[0] < score[1]: ans[1] += 48 * 60 - before

for i in range(2):
    print("%02d:%02d" %(ans[i] // 60, ans[i] % 60))'''

#17249: 태보태보 총난타
'''for s1 in list(input().split("(^0^)")):
    cnt = 0
    for s2 in s1:
        if s2 == '@': cnt += 1
    print(cnt, end = ' ')'''

#2774: 아름다운 수
'''for _ in range(int(input())):
    print(len(set(input())))'''

#11383: 뚊
'''n, m = map(int, input().split())
ans = []
for i in range(n):
    ans.append([])
    for s in input():
        ans[i].append(s * 2)

flag = True
for i in range(n):
    if ''.join(ans[i]) != input(): flag = False
    
print("Eyfa" if flag else "Not Eyfa")'''

#16955: 오목, 이길 수 있을까?
board = [list(input()) for _ in range(10)]
flag = False

for i in range(10):
    for j in range(10):
        if board[i][j] == 'X':
            for arr in [board[i][j : j + 5], 
                        [board[i + k][j + k] for k in range(5) if i + k < 10 and j + k < 10], 
                        [board[i - k][j - k] for k in range(5) if i - k >= 0 and j - k >= 0], 
                        [board[i + k][j] for k in range(5) if i + k < 10]]:
                if arr.count('X') == 4 and '.' in arr: 
                    flag = True
                    break
        if flag: break
    if flag: break

print(1 if flag else 0)

#16435: 스네이크 버드
'''n, m = map(int, input().split())
for num in sorted(list(map(int, input().split()))):
    if m >= num: m += 1
print(m)'''

#17608: 막대기
'''input = __import__('sys').stdin.readline

height = []
x = 0
cnt = 0

for _ in range(int(input())):
    height.append(int(input()))

for num in height[::-1]:
    if num > x: cnt += 1; x = num
print(cnt)'''

#3417: Vigenère Cipher Encryption
'''while True:
    key = input()
    if key == '0':
        break
    string = input()
    ans = ''
    for i in range(len(string)):
        ans += chr(((ord(string[i]) + ord(key[i % len(key)]) - 2 * ord('A') + 1) % 26 + ord('A')))
    print(ans)'''

#14623: 감정이입
'''x = int(input(), 2)
y = int(input(), 2)
print(bin(x * y)[2::])'''

#10865: 친구 친구
'''input = __import__('sys').stdin.readline

n, m = map(int, input().split())
arr = [0] * n

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1; b -=1
    arr[a] += 1; arr[b] += 1

print("\n".join(map(str, arr)))'''

#2164: 카드
'''from collections import deque
cards = deque([i for i in range(1, int(input()) + 1)])
while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())
print(*cards)'''