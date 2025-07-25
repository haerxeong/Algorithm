N, M = map(int, input().split())
baskets = [i for i in range(N + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    baskets[i: j+1] = baskets[j: i - 1: -1]
print(* baskets[1::])