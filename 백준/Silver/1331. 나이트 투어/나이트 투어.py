moves = [
    (1, 2), (2, 1), (-1, 2), (-2, 1),
    (1, -2), (2, -1), (-1, -2), (-2, -1)
]

def to_coord(s):
    return (ord(s[0]) - ord('A'), int(s[1]) - 1)

path = [to_coord(input().strip()) for _ in range(36)]

visited = set(path)
valid = True

if len(visited) != 36:
    valid = False

for i in range(35):
    x1, y1 = path[i]
    x2, y2 = path[i + 1]
    if (x2 - x1, y2 - y1) not in moves:
        valid = False
        break

x1, y1 = path[-1]
x2, y2 = path[0]
if (x2 - x1, y2 - y1) not in moves:
    valid = False

print("Valid" if valid else "Invalid")