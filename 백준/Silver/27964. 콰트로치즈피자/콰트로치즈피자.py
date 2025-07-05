N = int(input())
toppings = set(list(input().split()))
ans = 0

for i in toppings:
    if i[-6::] == 'Cheese':
        ans += 1

print('yummy' if ans >= 4 else 'sad')