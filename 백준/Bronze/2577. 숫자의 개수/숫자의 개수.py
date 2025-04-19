A = int(input())
B = int(input())
C = int(input())

res = str(A * B * C)
ans = [0] * 10

for i in res:
    ans[int(i)] += 1

print('\n'.join(map(str, ans)))