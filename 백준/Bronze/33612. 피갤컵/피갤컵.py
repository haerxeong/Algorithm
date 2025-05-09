N = int(input())

start_year = 2024
start_month = 8

total_month = (N - 1) * 7
final_year = start_year + (start_month + total_month - 1) // 12
final_month = (start_month + total_month - 1) % 12 + 1

print(final_year, final_month)