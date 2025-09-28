import sys
import bisect
input = sys.stdin.readline

N, Q = map(int, input().split())
c = list(map(int, input().split()))
t = list(map(int, input().split()))

# limit[i] = 농장을 방문하기 위해 S보다 작아야 하는 값
limit = [c[i] - t[i] for i in range(N)]
limit.sort()

for _ in range(Q):
    V, S = map(int, input().split())
    pos = bisect.bisect_right(limit, S)  # S보다 큰 값의 첫 위치
    can_visit = N - pos
    print("YES" if can_visit >= V else "NO")