N = int(input())
cnt = 0

i = 5
while N // i:
    cnt += N // i
    i *= 5

print(cnt)