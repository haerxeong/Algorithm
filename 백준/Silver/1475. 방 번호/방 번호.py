from collections import defaultdict

N = input()
dict = defaultdict(int)

for i in N:
    dict[int(i)] += 1

temp = dict[6] + dict[9]
dict[6], dict[9] = temp // 2, temp - temp // 2

print(max(dict.values()))