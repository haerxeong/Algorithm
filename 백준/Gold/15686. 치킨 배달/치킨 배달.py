from itertools import combinations as cb

N, M = map(int, input().split()) # N:그래프 크기, M: 치킨집 개수
city = [list(map(int, input().split())) for _ in range(N)] # 0: 빈칸, 1: 집, 2: 치킨집
chickens = []
ans = float('inf')

for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chickens.append([i, j])

for result in cb(chickens, M): # result: M개 치킨집 위치 배열
    distance = 0
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                temp = float('inf')
                for x, y in result:
                    temp = min(temp, abs(i - x) + abs(j - y))
                distance += temp

    ans = min(ans, distance)

print(ans)