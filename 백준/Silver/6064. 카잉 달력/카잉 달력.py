import math

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())

    lcm = M * N // math.gcd(M, N)  # 마지막 해(최대 범위)
    answer = -1

    k = x
    while k <= lcm:
        # y좌표 계산
        if (k - 1) % N + 1 == y:
            answer = k
            break
        k += M  # x는 항상 만족하므로 M씩만 증가

    print(answer)