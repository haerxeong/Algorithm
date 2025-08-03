D, K = map(int, input().split())

# 피보나치 수열의 계수 저장
fib = [0] * (D + 1)
fib[1] = 1
fib[2] = 1
for i in range(3, D + 1):
    fib[i] = fib[i - 1] + fib[i - 2]

# A * fib[D-2] + B * fib[D-1] = K 만족하는 A, B 탐색
for A in range(1, K + 1):
    temp = K - fib[D - 2] * A
    if temp % fib[D - 1] != 0:
        continue
    B = temp // fib[D - 1]
    if A <= B:
        print(A)
        print(B)
        break