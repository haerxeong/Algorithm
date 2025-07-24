input = __import__('sys').stdin.readline

N = int(input())
price = sorted([int(input()) for _ in range(N)], reverse=True)
ans = 0

for i in range(N):
    if i % 3 != 2:
        ans += price[i]

print(ans)