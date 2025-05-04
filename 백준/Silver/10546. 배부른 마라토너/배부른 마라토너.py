import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
people = [input().strip() for _ in range(N)]
leave = [input().strip() for _ in range(N - 1)]

enter_counter = Counter(people)
leave_counter = Counter(leave)

for name in enter_counter:
    if enter_counter[name] != leave_counter.get(name, 0):
        print(name)
        break