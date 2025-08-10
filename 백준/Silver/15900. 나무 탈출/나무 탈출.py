import sys
input = sys.stdin.readline

N = int(input())
g = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

# 1번을 루트로 깊이 합 계산(리프만)
stk = [(1, 0, 0)]  # (node, parent, depth)
ans = 0

while stk:
    u, p, d = stk.pop()
    is_leaf = (u != 1 and len(g[u]) == 1)
    if is_leaf:
        ans += d
        continue
    for v in g[u]:
        if v != p:
            stk.append((v, u, d + 1))

print("Yes" if ans % 2 == 1 else "No")