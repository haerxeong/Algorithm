input = __import__('sys').stdin.readline

N = int(input())
meeting = sorted([list(map(int, input().split())) for _ in range(N)], key = lambda arr: [arr[1], arr[0]])
last_time = cnt = 0

for i in range(N):
    if last_time <= meeting[i][0]:
        cnt += 1
        last_time = meeting[i][1]

print(cnt)