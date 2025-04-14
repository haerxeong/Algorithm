N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

t_shirts = 0

for i in sizes:
    t_shirts += i // T
    if i % T: t_shirts += 1

pens, pen = N // P, N % P

print(f"{t_shirts}\n{pens} {pen}")