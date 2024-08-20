#1100: 하얀 칸
'''arr = [list(input()) for _ in range(8)]
cnt = 0
for i in range(8):
    for j in range((i % 2), 8, 2):
        if arr[i][j] == 'F':
            cnt += 1
print(cnt)'''

#10864: 친구
'''n, m = map(int, input().split())

friends = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    friends[a].append(b)
    friends[b].append(a)

for i in range(n):
    print(len(friends[i]))'''

#2999: 비밀 이메일
'''message = input()
n = len(message)

div = []
for i in range(1, n + 1):
    if n % i == 0: 
        div.append(i)

if len(div) % 2 == 0:
    r = div[len(div) // 2 - 1]
    c = n // r
else:
    r = div[len(div) // 2]
    c = n // r 

matrix = [[' ']*c for _ in range(r)]

for j in range(c):
    for i in range(r):
        matrix[i][j] = message[r * j + i]
        
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end = '')'''

#12759: 틱! 택! 토!
'''player = int(input())
arr = [['-'] * 3 for _ in range(3)]
cnt = 0
winner = 0
while True:
    r, c = map(int, input().split())
    r -= 1; c -=1; cnt += 1

    if cnt % 2 == 0:
        arr[r][c] = 'o'
    else:
        arr[r][c] = 'x'

    temp = []

    for i in range(3):
        temp.append([arr[i][0], arr[i][1], arr[i][2]])

    for i in range(3):
        temp.append([arr[0][i], arr[1][i], arr[2][i]])

    temp.append([arr[0][0], arr[1][1], arr[2][2]])
    temp.append([arr[0][2], arr[1][1], arr[2][0]])

    if ['x', 'x', 'x'] in temp:
        winner = player
        
    elif ['o', 'o', 'o'] in temp:
        if player == 1:
            winner = 2
        else:
            winner = 1
        
    if winner != 0 or cnt == 9:
        break

print(winner)''' #내가혼자풀엇어ㅜ 
 

#2566: 최댓값
'''arr = []
for _ in range(9):
    arr.append(list(map(int, input().split())))

max_row = 0; max_col = 0; max_val = 0

for i in range(9):
    for j in range(9):
        if arr[i][j] > max_val:
            max_row = i; max_col = j; max_val = arr[i][j]

print(max_val)
print(max_row + 1, max_col + 1)'''

#5533: 유니크
'''n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

sum = [0] * n

for j in range(3): #각 라운드(열)에 대해
    for i in range(n): #각 플레이어(행)에 대해
        flag = True
        for k in range(n):
            if i == k:
                continue

            if arr[i][j] == arr[k][j]:
                flag = False
                break

        if flag:
            sum[i] += arr[i][j] #wow... count메소드를 썼다면,,,

for i in sum:
    print(i)'''

#10798: 세로읽기
'''arr = []
for _ in range(5):
    arr.append(list(input()))

for i in range(15):
    for j in range(5):
        try:
            print(arr[j][i], end = '')
        except IndexError:
            continue'''

#1018: 체스판 다시 칠하기
'''n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(input()))

ans = []

for i in range(n - 7):
    for j in range(m - 7):
        cnt1 , cnt2 = 0, 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'B':
                        cnt1 += 1
                    if board[k][l] != 'W':
                        cnt2 += 1
                else: 
                    if board[k][l] != 'W':
                        cnt1 += 1
                    if board[k][l] != 'B':
                        cnt2 += 1
        ans.append(cnt1)
        ans.append(cnt2)

print(min(ans))''' #k for문부터 구글의 힘. 근데 ㅈㄴ 맘에안듦 코드 개더러움

#1181: 단어 정렬
'''n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

arr = list(set(arr))
arr.sort(key = lambda x: [len(x), x])
for s in arr:
    print(s)'''

#10825: 국영수
'''arr = []
n = int(input())
for _ in range(n):
    name, x, y, z = input().split()
    arr.append([name, int(x), int(y), int(z)])

arr.sort(key = lambda x: [-x[1], x[2], -x[3], x[0]])

for i in range(n):
    print(arr[i][0])'''

#14592: 아주대학교 프로그래밍 경시대회 (Small) & (Large)
'''n = int(input())
arr = []
for i in range(n):
    score, cnt, time = map(int, input().split())
    arr.append((score, cnt, time, i + 1))

arr = sorted(arr, key = lambda x: [-x[0], x[1], x[2]])
print(arr[0][3])'''

#8979: 올림픽
'''n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key = lambda x: [x[1], x[2], x[3]], reverse = True)

rank = 1
for i in range(n):
    if arr[i][0] == k:
        print(rank)
        break

    if arr[i][1:] != arr[i + 1][1:]:
        rank = i + 2'''

#15905: 스텔라(STELLA)가 치킨을 선물했어요
'''n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key = lambda x: [-x[0], x[1]])

cnt = 0
std = arr[4][0]
for i in range(5, n):
    if arr[i][0] == std:
        cnt += 1

    else: break

print(cnt)'''

#2504: 괄호의 값
'''brackets = list(input())
val = 1
stack = []

for s in brackets:
    if len(stack) == 0:
        stack.append(s)
    else:
        if s == ']' and stack[-1] == '[':
            val ''' ######내가어케알아요잇

#7523: GauB
'''x = int(input())
for i in range(x):
    n, m = map(int, input().split())
    print(f"Scenario #{i + 1}:")
    print(f"{((m - n + 1) * (n + m) // 2)}\n")'''

##################
#2744: 대소문자 바꾸기
'''word = input()
ans = ''
for s in word:
    if ord("A") <= ord(s) <= ord("Z"):
        ans += s.lower()
    else:
        ans += s.upper()

print(ans)'''
###################

#7795: 먹을 것인가 먹힐 것인가_ㅂㅔ낌
'''for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
 
    a.sort()
    b.sort()
 
    count = 0
    pair = 0
 
    for i in range(n):
        while True:
            if count == m or a[i] <= b[count]:
                pair += count
                break
            else:
                count += 1
 
    print(pair)'''

#2729: 이진수 덧셈
t = int(input())
ans_lst = []

for i in range(t):
    A, B = input().split()
    sum = list(str(int(A) + int(B)))

    while '2' in sum or '3' in sum: 
        for j in range(len(sum)):
            if sum[-(j+1)] == '2':
                sum[-(j+1)] = '0'
                if j+2 <= len(sum):
                    sum[-(j+2)] = str(int(sum[-(j+2)]) + 1)
                if j+2 > len(sum):
                    sum.insert(0, '1')
          
            if sum[-(j+1)] == '3': 
                sum[-(j+1)] = '1'
                if j+2 <= len(sum):
                    sum[-(j+2)] = str(int(sum[-(j+2)]) + 1)
                if j+2 > len(sum):
                    sum.insert(0, '1')
          
    ans = int(''.join(sum))
    ans_lst.append(ans)
  
print(*ans_lst, sep = '\n')