#Brute_force

#13423: Three Dots
'''
from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    spotList = defaultdict(int)
    for i in range(n):              # 모든 점을 defaultdict에 담기
        spotList[arr[i]] = 1               # True를 의미함

    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            first = arr[i]
            second = arr[j]
            third = arr[j] + (arr[j] - arr[i]) # 임의의 세번 째 점
            if spotList[third] == 1:      # 임의의 세번 째 점이 존재하는지 확인
                ans += 1
    print(ans)
'''

#19532: 수학은 비대면강의입니다 
'''
flag = False
a, b, c, d, e, f = map(int, input().split())
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            flag = True
            break
    if flag: break

print(x, y)
'''

#20410: 추첨상 사수 대작전! (Easy) 
'''
m, seed, x1, x2 = map(int, input().split())
flag = False
for a in range(m):
    for c in range(m):
        if x1 == (a * seed + c) % m and x2 == (a * x1 + c) % m:
            flag = True
            break
    if flag: break
print(a, c)
'''

#3040: 백설 공주와 일곱 난쟁이
'''from itertools import combinations as cb

li = [int(input()) for _ in range(9)]

for x in cb(li, 7):
    if sum(x) == 100:
        print(*x, sep = '\n')'''

#1436: 영화감독 숌
'''
n = int(input())
cnt, i = 0, 1
while cnt != n:
    if '666' in str(i):
        cnt += 1
    i += 1

print(i - 1)
'''

#1969: DNA
'''from collections import defaultdict

s = ''
n, m = map(int, input().split())
DNA = [list(input()) for _ in range(n)] #열끼리볼까... 여기서 브루트포스를 어떻게 쓰지? 딕셔너리? 디폴트딕?

for j in range(m):
    dict = defaultdict(int)
    
    for i in range(n):
        dict[DNA[i][j]] += 1
    
    max_cnt = max(dict.values())
    
    for nu in ["A", "C", "G", "T"]:
        if dict[nu] == max_cnt:
            s += nu
            break

hamming_dist = 0
for i in range(n):
    for j in range(m):
        if DNA[i][j] != s[j]:
            hamming_dist += 1

print(s)
print(hamming_dist)'''

#1018: 체스판 다시 칠하기
#어려워!!!!!!!!!!!!!!!!!!!
'''n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
chess = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']

min_cnt = 64

for i in range(n - 7):
    for j in range(m - 7): #왼쪽끝점
        cnt = 0
        for k in range(i, i+8):
            print(f"change k = {k}")
            for x, y in zip(board[i][j:j+8], chess):
                if k % 2 == 1: print(x, y)
                if k % 2 == 0 and x != y: cnt += 1; print(1, end = '')
                if k % 2 == 1 and x == y: cnt += 1; print(1, end = '')
            print("\n한줄변화량", cnt)
        min_cnt = min(min_cnt, cnt, 64 - cnt)

print(min_cnt)'''

#retry
'''n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
chess = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']

min_cnt = 64

for i in range(n - 7):
    for j in range(m - 7): #왼쪽끝점
        cnt = 0
        for k in range(i, i+8):
            for x, y in zip(board[k][j:j+8], chess):
                if k % 2 == 0 and x != y: cnt += 1
                if k % 2 == 1 and x == y: cnt += 1
        min_cnt = min(min_cnt, cnt, 64 - cnt)

print(min_cnt)'''

#1895: 필터
'''r, c = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(r)]
t = int(input())
J = []

for i in range(r - 2):
    for j in range(c - 2): #왼쪽끝점
        filter = []
        for k in range(i, i + 3):
            for l in range(j, j + 3):
                filter.append(li[k][l])
        J.append(sorted(filter)[4])

print(sum(1 for i in J if i >= t))'''

#10974: 모든 순열
'''from itertools import permutations as pm

N = int(input())
for x in pm([i for i in range(1, N + 1)], N):
    print(*x)'''

#17626: Four Squares
'''n = int(input())

if int(n**0.5)**2 == n:
    print(1)

else:
    #2인 경우
    for i in range(int(n**0.5), 0, -1):
        for j in range(int((n-i**2)**0.5), 0, -1):
            if n == i**2 + j**2:
                print(2)
                break
            for k in range(int((n - i**2 - j**2)**0.5), 0, -1):
                if n == i**2 + j**2:
                    pass'''
#?
'''def go(arr):
    if sum(arr) == n:
        return
    else
n = int(input())
li = [i for i in range(int(n**0.5), 0, -1)]'''

#???또시도
def isSqure(n):
    if int(n**0.5)**2 == n: return True
    return False

def squares(n):
    if isSqure(n): return 1

    for i in range(int(n**0.5), 0, -1): #n을 i와 m으로 나눔
        m = n - i**2 #i는 이미 제곱!
        if isSqure(m): return 2
    
    for i in range(int(n**0.5), 0, -1): #n을 i와 m으로 나눔
        m = n - i**2 #i는 이미 제곱!
        for j in range(int(m**0.5), 0, -1): #n을 i와 m으로 나누고 m을 또 j와 l로 나눔, 즉 n을 i, j, l로 나눔
            l = m - j**2
            if isSqure(l): return 3
    return 4

n = int(input())
print(squares(n))


#1057: 토너먼트
'''def new_number(n):
    if n % 2 == 0:
        return n // 2
    else:
        return (n + 1) // 2
    
N, kim, lim = map(int, input().split())
round = 1

while N > 1:
    if abs(kim - lim) == 1 and max(kim, lim) % 2 == 0: break

    kim = new_number(kim)
    lim = new_number(lim)
    N //= 2

    round += 1

print(round)'''

#15654: N과 M (5)
'''def go(arr):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    for i in li:
        if not arr or i not in arr:
            arr.append(i)
            go(arr)
            arr.pop()

N, M = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
go([])
'''

#15651: N과 M (3)
'''def go(arr):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    for i in li:
        arr.append(i)
        go(arr)
        arr.pop()

N, M = map(int, input().split())
li = [i for i in range(1, N + 1)]
go([])'''

#15655: N과 M (6)
'''def go(arr):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    for i in li:
        if not arr or arr[-1] < i:
            arr.append(i)
            go(arr)
            arr.pop()

N, M = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
go([])'''

#9095번: 1, 2, 3 더하기
'''def go(arr):
    global cnt

    if sum(arr) == n:
        cnt += 1
        return 
    
    for i in [1, 2, 3]:
        if not arr or sum(arr) + i <= n:
            arr.append(i)
            go(arr)
            arr.pop()

    return cnt

for _ in range(int(input())):
    n = int(input())
    cnt = 0
    print(go([]))   
'''

#14888번: 연산자 끼워넣기
#백트래킹으로 풀려고 했는데... 못하겟으요...
'''def go(arr):
    if sum(op) == 0:
        ans.append()
        return
    
    for i in A:
        arr.append(i)
        for x, y in zip(op, op_num):
            if op_num:
                arr.append(i)


N = int(input())
A = list(map(int, input().split()))
op_num = list(map(int, input().split()))
op = ['+', '-', '*', '/']
ans = []
go([])

#순열로 재시도
#이것도 못하겠는디
from itertools import permutations as pm

def calculate(op)

N = int(input())
A = list(map(int, input().split()))

for x in pm(['+', '-', '*', '/'], N-1):
    pass

#다시 백트래킹 도전... -> 딱 한 번만 됨...
def Flag(op):
    if op == '+': return 0
    elif op == '-': return 1
    elif op == '*': return 2
    else: return 3

def calculate(arr):
    ret = A[0]

    for i in range(N - 1):
        if arr[i] == '+':
            ret += A[i + 1]
        elif arr[i] == '-':
            ret -= A[i + 1]
        elif arr[i] == '*':
            ret *= A[i + 1]
        else: ret /= A[i + 1]

    return ret

def go(arr):
    if sum(op) == 0:
        ans.append(calculate(arr))
        print(f"결과 확인용: {arr}")
        return
    
    for x in ['+', '-', '*', '/']:
        flag = Flag(x)

        if op[flag]:
            arr.append(x)
            op[flag] -= 1

            go(arr)
            arr.pop()

N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))

ans = []

go([])

print(max(ans))
print(min(ans))

#다시!!!
from itertools import permutations as pm

def calculate(arr):
    ret = A[0]

    for i in range(N - 1):
        if arr[i] == '+':
            ret += A[i + 1]
        elif arr[i] == '-':
            ret -= A[i + 1]
        elif arr[i] == '*':
            ret *= A[i + 1]
        else: ret = int(ret / A[i + 1])

    return ret

N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))

op_list = ['+'] * op[0] + ['-'] * op[1] + ['*'] * op[2] + ['/'] * op[3]
op_pm = set()
ans = []

for x in pm(op_list, N-1):
    op_pm.add(x)

for x in op_pm:
    ans.append(calculate(x))

print(max(ans))
print(min(ans))'''

