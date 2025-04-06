for _ in range(int(input())):
    control = input()
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    d = 0 # dx, dy의 index
    
    x, y = 0, 0
    x_history, y_history = {0}, {0}

    for s in control:
        if s == "F":
            x += dx[d]; y += dy[d]
        elif s == "B":
            x -= dx[d]; y -= dy[d]
        elif s == "L":
            d = (d + 3) % 4
        else:
            d = (d + 1) % 4
        
        x_history.add(x)
        y_history.add(y)

    print((max(x_history) - min(x_history)) * (max(y_history) - min(y_history)))
