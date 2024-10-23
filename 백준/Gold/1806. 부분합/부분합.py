N, S = map(int, input().split())
li = list(map(int, input().split()))
minLen = float('inf')
partSum = li[0]

if sum(li) < S:
    print(0)
else:
    left, right = 0, 0
    while left <= right < N:
        if partSum >= S:
            minLen = min(minLen, right - left + 1)
            partSum -= li[left]
            left += 1
        else:
            if right + 1 < N: partSum += li[right + 1]
            right += 1

    print(minLen)