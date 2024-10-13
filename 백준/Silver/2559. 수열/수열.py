N, K = map(int, input().split())
li = list(map(int, input().split()))
left, right = 0, K - 1
temp = sum(li[left : right])
max_value = temp + li[right]

while right < N:
    temp += li[right]
    max_value = max(max_value, temp)
    temp -= li[left]

    left += 1
    right += 1

print(max_value)