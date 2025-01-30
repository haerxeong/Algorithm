for _ in range(int(input())):
    N = int(input())
    note1 = sorted(list(map(int, input().split()))) # 연종이가 본
    M = int(input())
    note2 = list(map(int, input().split())) # 연종이가 질문 던진

    ans = [0] * M

    for i in range(M):
        left, right = 0, N - 1
        val = note2[i]

        while left <= right:
            mid = (left + right) // 2

            if note1[mid] == val:
                ans[i] = 1
                break

            elif note1[mid] > val:
                right = mid - 1

            else:
                left = mid + 1

    print('\n'.join(map(str, ans)))