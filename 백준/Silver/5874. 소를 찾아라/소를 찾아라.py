s = input().strip()
count_open = 0  # 지금까지 나온 "((" 개수
ans = 0

for i in range(len(s) - 1):
    pair = s[i:i+2]
    if pair == "((":
        count_open += 1
    elif pair == "))":
        ans += count_open

print(ans)