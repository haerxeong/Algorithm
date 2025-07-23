N = int(input())
t = sorted(list(map(int, input().split())), reverse=True)
last = t[0] + 2
for i in range(1, N):
    last = max(last, t[i] + i + 2)
print(last)