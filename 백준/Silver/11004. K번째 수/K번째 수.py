input = __import__('sys').stdin.readline

N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
print(A[K - 1])