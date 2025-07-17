sum = 0
scores = [int(input()) for _ in range(10)]

for i in range(10):
    if sum + scores[i] < 100:
        sum += scores[i]
    else:
        if 100 - sum < sum + scores[i] - 100:
            break
        else:
            sum += scores[i]
            break

print(sum)