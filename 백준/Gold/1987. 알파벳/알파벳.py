import sys

# 입력 처리
R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최대 방문할 수 있는 칸 개수
max_count = 0

def dfs(x, y, visited, count):
    global max_count
    max_count = max(max_count, count)

    # 4방향 탐색
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < R and 0 <= ny < C:
            char_index = ord(board[nx][ny]) - ord('A')

            if not (visited & (1 << char_index)):  # 방문한 적 없으면 이동
                dfs(nx, ny, visited | (1 << char_index), count + 1)

# 초기 상태에서 DFS 시작
start_char = ord(board[0][0]) - ord('A')
dfs(0, 0, 1 << start_char, 1)

# 결과 출력
print(max_count)