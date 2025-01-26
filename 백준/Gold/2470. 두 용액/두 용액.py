N = int(input())
li = sorted(list(map(int, input().split())))

left, right = 0, N - 1
min_sum = abs(li[left] + li[right])
ans = [li[left], li[right]]

while left < right:
    if min_sum > abs(li[left] + li[right]):
        min_sum = abs(li[left] + li[right])
        ans = [li[left], li[right]]
    
    if li[left] + li[right] >= 0:
        right -= 1
    else:
        left += 1

print(*ans)