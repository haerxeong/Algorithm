N = int(input())
li = sorted(list(map(int, input().split())))
min_value = float('inf')
ans = []

for i in range(N):
    left, right = 0, N - 1

    while left < right:
        if left == i: left += 1
        elif right == i: right -= 1
        else:
            target = abs(li[i] + li[left] + li[right])

            if target < min_value:
                min_value = target
                ans = [li[i], li[left], li[right]]

            if target == 0:
                break     
            elif li[i] + li[left] + li[right] < 0:
                left += 1
            else:
                right -= 1

print(' '.join(map(str, sorted(ans))))