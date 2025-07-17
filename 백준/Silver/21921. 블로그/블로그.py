N, X = map(int, input().split())
visit = list(map(int, input().split()))
prefix, period = 0, 1

for i in range(N):
    if i < X:
        prefix += visit[i]
        max_visit = prefix
    else:
        prefix = prefix - visit[i - X] + visit[i]
        if max_visit < prefix:
            max_visit = prefix
            period = 1
        elif max_visit == prefix:
            period += 1

print("SAD" if not max_visit else f"{max_visit}\n{period}")