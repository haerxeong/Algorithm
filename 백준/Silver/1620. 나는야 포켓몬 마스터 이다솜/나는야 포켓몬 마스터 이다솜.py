N, M = map(int, input().split()) # N: 포켓몬의 수, M: 문제의 수
poketmons = dict()
poketmon_names = dict()
for i in range(N):
    name = input()
    poketmons[i + 1] = name
    poketmon_names[name] = i + 1

for i in range(M):
    problem = input()
    if problem < 'A':
        print(poketmons[int(problem)])
    else:
        print(poketmon_names[problem])