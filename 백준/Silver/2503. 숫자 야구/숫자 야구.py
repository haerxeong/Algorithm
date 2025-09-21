from itertools import permutations

def check(candidate, guess, s, b):
    strike = sum(a == b for a, b in zip(candidate, guess))
    ball = len(set(candidate) & set(guess)) - strike
    return strike == s and ball == b

N = int(input())
queries = []
for _ in range(N):
    num, s, b = input().split()
    queries.append((list(num), int(s), int(b)))

count = 0
for cand in permutations("123456789", 3):  # 가능한 세자리 수
    if all(check(cand, q[0], q[1], q[2]) for q in queries):
        count += 1

print(count)