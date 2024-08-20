#Binary_Search
#1654번: 랜선 자르기
'''K, N = map(int, input().split())
lengths = sorted([int(input()) for _ in range(K)])
left, right = 1, lengths[-1]

while left <= right:
    cnt = 0
    mid = (left + right) // 2
    for length in lengths:
        cnt += length // mid
    
    if cnt >= N:
        maxLen = mid
        left = mid + 1
    
    else:
        right = mid - 1

print(maxLen)'''

#16401번: 과자 나눠주기
'''M, N = map(int, input().split())
L = sorted(list(map(int, input().split())))
left, right = 1, L[-1]
result = 0

while left <= right:
    cnt = 0
    mid = (left + right) // 2
    for length in L:
        cnt += length // mid

    if cnt >= M:
        result = mid
        left = mid + 1
    else:
        right = mid - 1 

print(result)'''

#14627번: 파닭파닭
'''S, C = map(int, input().split())
L = sorted([int(input()) for _ in range(S)])
left, right = 1, L[-1]

while left <= right:
    mid = (left + right) // 2
    cnt = sum(length // mid for length in L)

    if cnt >= C:
        res = mid
        left = mid + 1
    else:
        right = mid - 1

print(sum(L) - res * C)'''

#6236번: 용돈 관리
'''N, M = map(int, input().split())
amount = sorted([int(input()) for _ in range(N)])
left, right = 1, amount[-1]

while left <= right:
    mid = (left + right) // 2
    cnt = sum(i // mid for i in amount)

    if cnt >= M:
        K = mid
        left = mid + 1
    else:
        right = mid - 1

print(K)'''

'''N, M = map(int, input().split())
amount = sorted([int(input()) for _ in range(N)])
left, right = 1, amount[-1]

while left <= right:
    mid = (left + right) // 2
    cnt, current = 1, mid
    for i in amount:
        if current - mid > 0:
            current - mid
        else:
            cnt += 1
            current += mid

    if cnt <= M:
        K = mid
        rignt = mid - 1
    else:
        left = mid + 1

print(K)'''

#2343번: 기타 레슨
'''N, M = map(int, input().split())
lengths = sorted(list(map(int, input().split())))'''


#누적합
#11659번: 구간 합 구하기 4
'''N, M = map(int, input().split())
li = list(map(int, input().split()))
for _ in range(M):
    i, j = map(int, input().split())
    print(sum(li[i - 1 : j]))'''

#test
#
N, M, K = map(int, input().split())
board = [[0]*M] + [[0] + list(input().strip()) for _ in range(N)]

check_W = ["0"*(M+1)] + ["0" + "WB"*(M//2) + "W"*(M%2), "0" + "BW"*(M//2) + "B"*(M%2)]*(N//2) + ["0" + "WB"*(M//2) + "W"*(M%2)]*(N%2)
check_B = ["0"*(M+1)] + ["0" + "BW"*(M//2) + "B"*(M%2), "0" + "WB"*(M//2) + "W"*(M%2)]*(N//2) + ["0" + "BW"*(M//2) + "B"*(M%2)]*(N%2)

sum_sub_W = [[0]*(M+1) for _ in range(N+1)]
sum_sub_B = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        sum_sub_W[i][j] = int(board[i][j] != check_W[i][j]) + sum_sub_W[i-1][j] + sum_sub_W[i][j-1] - sum_sub_W[i-1][j-1]
        sum_sub_B[i][j] = int(board[i][j] != check_B[i][j]) + sum_sub_B[i-1][j] + sum_sub_B[i][j-1] - sum_sub_B[i-1][j-1]

result = float("inf")
for x_start in range(1, N-K+2):
    for y_start in range(1, M-K+2):
        x_point = x_start+K-1
        y_point = y_start+K-1
        
        cnt_color_W = sum_sub_W[x_point][y_point] - sum_sub_W[x_start-1][y_point] - sum_sub_W[x_point][y_start-1] + sum_sub_W[x_start-1][y_start-1]
        cnt_color_B = sum_sub_B[x_point][y_point] - sum_sub_B[x_start-1][y_point] - sum_sub_B[x_point][y_start-1] + sum_sub_B[x_start-1][y_start-1]
        
        result = min(result, cnt_color_W, cnt_color_B)

print(result)

#1208번: 부분수열의 합2
'''N, S = map(int, input().split())
li = list(map(int, input().split()))
left, right = 0, li[-1]

while left <= right:
    mid = (left + right) // 2'''
