N = int(input())
scores = sorted(list(map(int, input().split())))
M = scores[-1]
sum = 0

for i in range(N):
    sum += scores[i] / M * 100

print(sum / N)