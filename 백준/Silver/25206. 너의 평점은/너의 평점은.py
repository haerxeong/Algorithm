sum = 0
num = 0
for i in range(20):
    subject, weight, grade = input().split()
    weight = float(weight)
    if grade == 'A+': sum += 4.5 * weight
    elif grade == 'A0': sum += 4.0 * weight
    elif grade == 'B+': sum += 3.5 * weight
    elif grade == 'B0': sum += 3.0 * weight
    elif grade == 'C+': sum += 2.5 * weight
    elif grade == 'C0': sum += 2.0 * weight
    elif grade == 'D+': sum += 1.5 * weight
    elif grade == 'D0': sum += 1.0 * weight
    elif grade == 'P': continue
    num += weight

print(sum / num)