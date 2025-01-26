while True:
    N, M = map(int, input().split())
    
    if N == M == 0: break

    sanggeuns = [int(input()) for _ in range(N)]
    sunyeongs = [int(input()) for _ in range(N)]

    pointer1, pointer2 = 0, 0
    same_cds = 0

    while pointer1 < N and pointer2 < M:
        if sanggeuns[pointer1] == sunyeongs[pointer2]:
            same_cds += 1
            pointer1 += 1
            pointer2 += 1
        elif sanggeuns[pointer1] > sunyeongs[pointer2]:
            pointer2 += 1
        else: # one < two:
            pointer1 += 1

    print(same_cds)