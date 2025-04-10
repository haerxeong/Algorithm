not_self_number = set()

for i in range(1, 10):
    not_self_number.add(i + i)

for i in range(10, 100):
    not_self_number.add(i + i//10 + i%10)

for i in range(100, 1000):
    not_self_number.add(i + i//100 + (i%100)//10  + i%10)

for i in range(1000, 10000):
    not_self_number.add(i + i//1000 + (i%1000)//100 + (i%100)//10 + i % 10)

for i in range(1, 10000):
    if i not in not_self_number: print(i)