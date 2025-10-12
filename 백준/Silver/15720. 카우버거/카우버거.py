B, C, D = map(int, input().split())
burgers = sorted(list(map(int, input().split())), reverse=True)
sides = sorted(list(map(int, input().split())), reverse=True)
drinks = sorted(list(map(int, input().split())), reverse=True)

total = sum(burgers) + sum(sides) + sum(drinks)
sets = min(B, C, D)
discount = 0
for i in range(sets):
    discount += (burgers[i] + sides[i] + drinks[i]) * 0.9

discount += sum(burgers[sets:]) + sum(sides[sets:]) + sum(drinks[sets:])

print(total)
print(int(discount))