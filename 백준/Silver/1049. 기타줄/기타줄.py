N, M = map(int, input().split())
package = each = float('inf')
price = 0

for _ in range(M):
    p, e = map(int, input().split())
    package = min(package, p)
    each = min(each, e)

while N:
    if N >= 6:
        if package < 6 * each:
            price += package
        else:
            price += 6 * each
        N -= 6
    else:
        if package < N * each:
            price += package
        else:
            price += N * each
        break

print(price)