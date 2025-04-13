n, m = map(int, input().split())
pay = list(map(int, input().split()))

if m == 0:
    print(0)
    exit()

current_sum = sum(pay[:m])
max_sum = current_sum

# 슬라이딩 윈도우
for i in range(m, n):
    current_sum += pay[i] - pay[i - m]
    max_sum = max(max_sum, current_sum)

print(max_sum)