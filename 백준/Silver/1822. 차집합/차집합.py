nA, nB = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

A_B = sorted(A - B)

print(f"{len(A_B)}\n{' '.join(map(str, A_B))}" if A_B else 0)