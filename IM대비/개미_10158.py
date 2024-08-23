def gaemi(w, h, p, q, t):
    # 가로 좌표 계산
    new_x = (p + t) % (2 * w)
    if new_x > w:
        new_x = 2 * w - new_x

    # 세로 좌표 계산
    new_y = (q + t) % (2 * h)
    if new_y > h:
        new_y = 2 * h - new_y

    return new_x, new_y

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x, y = gaemi(w, h, p, q, t)
print(x, y)