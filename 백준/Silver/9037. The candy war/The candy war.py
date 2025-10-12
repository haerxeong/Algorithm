def make_even(candies):
    # 모든 사탕을 짝수로 만듦
    for i in range(len(candies)):
        if candies[i] % 2 == 1:
            candies[i] += 1
    return candies

def all_equal(candies):
    return len(set(candies)) == 1

def simulate(candies):
    candies = make_even(candies)
    count = 0

    while not all_equal(candies):
        new_candies = [0] * len(candies)

        for i in range(len(candies)):
            give = candies[i] // 2  # 반을 오른쪽으로 줌
            new_candies[i] -= give
            new_candies[(i + 1) % len(candies)] += give

        for i in range(len(candies)):
            candies[i] += new_candies[i]
            if candies[i] % 2 == 1:
                candies[i] += 1

        count += 1

    return count

T = int(input())
for _ in range(T):
    N = int(input())
    candies = list(map(int, input().split()))
    print(simulate(candies))