N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split())) # 동 1 서 2 북 3 남 4

dice = [0] * 6 # 윗면: dice[0], 바닥: dice[-1]

for c in commands:
    if c == 1 and y + 1 < M:
        y += 1
        new_dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif c == 2 and y - 1 >= 0:
        y -= 1
        new_dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif c == 3 and x - 1 >= 0:
        x -= 1
        new_dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    elif c == 4 and x + 1 < N:
        x += 1
        new_dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    else: # 넘어가려고함
        continue

    if not board[x][y]:
        board[x][y] = new_dice[-1]
    else:
        new_dice[-1] = board[x][y]
        board[x][y] = 0

    print(new_dice[0])
    dice = new_dice