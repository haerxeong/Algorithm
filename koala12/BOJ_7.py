#15874: Caesar Cipher
'''n, l = map(int, input().split())
n %= 26
string = input()
ans = ''
for s in string:
    if ord('A') <= ord(s) <= ord('Z'):
        s = chr(((ord(s) - ord('A') + n) % 26) + ord('A'))
    elif ord('a') <= ord(s) <= ord('z'):
        s = chr(((ord(s) - ord('a') + n) % 26) + ord('a'))
    ans += s

print(ans)'''

#11655: ROT13
'''string = input()
ans = ''
for s in string:
    if 'A' <= s <= 'Z':
        s = chr(((ord(s) - ord('A') + 13) % 26) + ord('A'))
    elif 'a' <= s <= 'z':
        s = chr(((ord(s) - ord('a') + 13) % 26) + ord('a'))
    ans += s

print(ans)'''

#11575: Affine Cipher
'''input = __import__('sys').stdin.readline
for _ in range(int(input())):
    a, b = map(int, input().strip().split())
    string = list(input().strip())
    for i in range(len(string)):
        string[i] = chr(((a * (ord(string[i]) - 65) + b) % 26) + 65)
    print(''.join(string))'''

#1718: 암호 
'''s = input()
code = input()
ans = ''

for i in range(len(s)):
    key = ord(code[i % len(code)]) - ord('a') + 1

    if s[i] == ' ':
        ans += ' '
    else:
        ans += chr(((ord(s[i]) - ord('a') + 26 - key) % 26) + ord('a'))

print(ans)'''

#10974: 모든 순열
'''from itertools import permutations as pm

n = int(input())
arr = [i for i in range(1, n + 1)]

for x in pm(arr, n):
    print(' '.join(map(str, x)))'''

#2798: 블랙잭
'''from itertools import combinations as cb

n, m = map(int, input().split())
cards = list(map(int, input().split()))
ans = [0]

for x in cb(cards, 3):
    if ans[-1] < sum(x) <= m: 
        ans.append(sum(x))

print(ans[-1])'''

#15649: N과 M(1)
'''from itertools import permutations as pm

n, m = map(int, input().split())

for x in pm([i for i in range(1, n + 1)], m):
    print(' '.join(map(str, x)))'''

#15650: N과 M(2)
'''from itertools import permutations as pm

n, m = map(int, input().split())

for x in pm([i for i in range(1, n + 1)], m):
    if list(x) == sorted(x):
        print(' '.join(map(str, x)))'''

#1182: 부분수열의 합
'''from itertools import combinations as cb

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for i in range(1, n + 1):
    for x in cb(arr, i):
        if sum(x) == s: cnt += 1

print(cnt)'''

#15652: N과 M(4)
'''n, m = map(int, input().split())

i = 1; j = 1
while i < m + 1:
    for i in range(m):
        print(j, end = ' ')
        j += 1
    print()
    i += 1; j = i''' #dfs라는데 전 이건 못하겠네요..
        

#10102: 개표
'''v = int(input())
vote = list(input())

voteA, voteB = vote.count('A'), vote.count('B')
if voteA > voteB: print('A')
elif voteA < voteB: print('B')
else: print('Tie')'''

#2309: 일곱 난쟁이
'''from itertools import combinations as cb
h = [int(input()) for _ in range(9)]

for x in cb(h, 7):
    if sum(x) == 100:
        print('\n'.join(map(str, sorted(x))))
        break'''

#11880: 개미
'''input = __import__('sys').stdin.readline
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    m = max(arr)
    arr.remove(m)
    print((sum(arr)) ** 2 + m ** 2)'''

#12789: 도키도키 간식드리미
'''n = int(input())
wait = list(map(int, input().split()))
find = 1; stack = []
while wait:
    if wait[0] == find:
        wait.pop(0); find += 1
    else: stack.append(wait.pop(0))

    while stack:
        if stack[-1] == find:
            stack.pop()
            find += 1
        else: break

if len(stack) == 0:
    print("Nice")
else: print("Sad")'''

#2902: KMP는 왜 KMP일까?
'''for s in list(input().split('-')):
    print(s[0], end = '')'''

#4447: 좋은놈 나쁜놈
'''n = int(input())
for _ in range(n):
    name = input()
    print(name, 'is', end = ' ')
    g, b = name.lower().count('g'), name.lower().count('b')
    if g > b: print('GOOD')
    elif g < b: print("A BADDY")
    else: print("NEUTRAL")'''

#4072: Words
'''while True:
    letters = list(input().split())
    if letters[0] == "#": break
    for s in letters:
        print(s[::-1], end = ' ')'''
    
#15351: 인생 점수
'''n = int(input())
for _ in range(n):
    name = input()
    sum = 0
    for s in name:
        if s != ' ': sum += ord(s) - 64
    print("PERFECT LIFE" if sum == 100 else sum)'''

#1032: 명령 프롬포트
'''n = int(input())
file = [input() for _ in range(n)]
pat = ''
for j in range(len(file[0])):
    std = file[0][j]; flag = True
    for i in range(1, n):
        if file[i][j] != std: flag = False; break
    if flag: pat += std
    else: pat += '?'

print(pat)'''

#14581: 팬들에게 둘러싸인 홍준
#print(f''':fan::fan::fan:
#:fan::{input()}::fan:
#:fan::fan::fan:''')

################test
#12840: 창용이의 시계
'''h, m, s = map(int, input().split())
for _ in range(int(input())):
    query = list(map(int, input().split()))
    if query[0] == 1:
        s += query[1]
        h += s // 3600; s %= 3600
        m += s // 60; s %= 60
        
    elif query[0] == 2:
        h -= query[1] // 3600; query[1] %= 3600
        m -= 2; s += (120 + query[1])
        m -= s // 60; s %= 60

    else: 
        if h < 0: h += 12
        if m < 0: h -= 1; m += 60
        print(h, m, s)'''

#11866: 요세푸스 문제 0
n, k = map(int, input().split())
arr = [i for i in range(n)]
ans = []
while not arr:
    index = k
    ans.append(arr.pop(k) + 1)
    index = 2 * k % k

print(*ans) #ㅁㄹ겟다시봉방거