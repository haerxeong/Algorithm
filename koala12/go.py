def case1(i, j): #가로
    if j >= 6:
        return board[i][j - 1::]
    return board[i][j : j + 5]

def case2(i, j): #세로
    if i >= 6:
        return [board[i - 1 + k][j] for k in range(11 - i)]
    return [board[i + k][j] for k in range(5)]

def case3(i, j): #우하향대각선
    if i == 6 or j == 6: i -= 1; j -= 1
    if i <= 5 and j <= 5: 
        return [board[i + k][j + k] for k in range(5)] 
    return []

def case4(i, j): #좌하향대각선
    if i == 6 or j == 3: i -= 1; j += 1
    if i <= 5 and j >= 4:
        return [board[i + k][j - k] for k in range(5)]
    return []

board = [list(input()) for _ in range(10)]
flag = False

for i in range(10):
    #print(f"\ni: {i} 진행중...")
    for j in range(10):
        #print(f"j: {j} 진행중...")
        if board[i][j] == 'X':
            #print('X 확인 완료...')
            for arr in [case1(i,j), case2(i,j), case3(i,j), case4(i,j)]:
                if arr.count('X') == 4 and '.' in arr: 
                    flag = True
                    #print("about break...")
                    break
        if flag: break
    if flag: break

print(1 if flag else 0)