n = int(input())
houses = list(map(int, input().split()))

houses.sort()
print(houses[(n - 1) // 2])  # 중앙값 (짝수면 더 작은 쪽)