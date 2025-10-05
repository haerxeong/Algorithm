import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
arr = list(map(int, input().split()))

# prefix XOR 계산
prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] ^ arr[i - 1]

ans = 0
for _ in range(Q):
    s, e = map(int, input().split())
    ans ^= (prefix[e] ^ prefix[s - 1])

print(ans)