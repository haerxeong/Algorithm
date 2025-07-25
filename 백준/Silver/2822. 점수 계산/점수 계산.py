arr = sorted([[int(input()), i + 1] for i in range(8)], reverse = True)
score, problem = 0, []

for i in range(5):
    score += arr[i][0]
    problem.append(arr[i][1])

print(score)
print(*sorted(problem))