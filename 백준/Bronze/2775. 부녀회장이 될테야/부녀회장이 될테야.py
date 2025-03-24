for _ in range(int(input())):
    k = int(input())  # k층
    n = int(input())  # n호

    # 0층 초기화 (1호~n호까지 각각 1, 2, 3, ..., n)
    arr = [[0] * (n + 1) for _ in range(k + 1)]
    
    for j in range(1, n + 1):
        arr[0][j] = j

    # 층별 인원 계산
    for i in range(1, k + 1):  # 1층부터 k층까지
        for j in range(1, n + 1):  # 1호부터 n호까지
            if j == 1:
                arr[i][j] = arr[i - 1][j]  # 1호는 항상 위층의 같은 호 수만큼 거주
            else:
                arr[i][j] = arr[i][j - 1] + arr[i - 1][j]  # 이전 호 + 위층 같은 호

    print(arr[k][n])  