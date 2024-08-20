#11659: 구간 합 구하기 4
'''n, m = map(int, input().split())
n_list = list(map(int, input().split()))
for _ in range(m):
    i, j = map(int, input().split())
    print(sum(n_list[i -1 : j]))''' #시간초과
import sys
input=sys.stdin.readline
n, m = map(int, input().split())
n_list = list(map(int, input().split()))
sum_list = [0] * (n + 1)
for i in range(1, n + 1):
    sum_list[i] = sum_list[i - 1] + n_list[i - 1]
for _ in range(m):
    i, j = map(int, input().split())
    print(sum_list[j] - sum_list[i - 1])