def isBingo():
    cnt = 0
    
    # 가로
    for i in range(5):
        if not sum(board[i]): 
            cnt += 1

    #세로
    for i in range(5):
        temp = 0
        for j in range(5):
            temp += board[j][i]
        if not temp: cnt += 1

    # 대각선
    temp = 0
    for i in range(5):
        temp += board[i][i]
    if not temp: cnt += 1

    temp = 0
    for i in range(5):
        temp += board[i][4 - i]
    if not temp: cnt += 1

    if cnt >= 3: return True
    return False

def replace(current, dest):
    for i in range(5):
        for j in range(5):
            if board[i][j] == current:
                board[i][j] = dest
                break

board = [list(map(int, input().split())) for _ in range(5)]
nums = [list(map(int, input().split())) for _ in range(5)]

for i in range(5):
    for j in range(5):
        replace(nums[i][j], 0)
        if isBingo():
            print(i * 5 + j + 1)
            exit()