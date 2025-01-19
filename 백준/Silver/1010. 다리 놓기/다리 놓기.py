for _ in range(int(input())):
    N, M = map(int, input().split())
    M_factorial, N_factorial, M_N_factorial = 1, 1, 1
    
    for i in range(2, M + 1): M_factorial *= i
    for i in range(2, N + 1): N_factorial *= i
    for i in range(2, M - N + 1): M_N_factorial *= i

    print(M_factorial // (M_N_factorial * N_factorial))