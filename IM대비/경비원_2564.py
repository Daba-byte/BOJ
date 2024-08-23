def bbiyong(w, h, store):
    # 북쪽
    if store[0] == 1:
        return w + h + (w - store[1])
    # 남쪽
    if store[0] == 2:
        return store[1]
    # 서쪽
    if store[0] == 3:
        return 2 * w + h + store[1]
    # 동쪽
    if store[0] == 4:
        return w + (h - store[1])


w, h = map(int, input().split())
n = int(input())
store_list = []
for _ in range(n):
    a, b = list(map(int, input().split()))
x, y = map(int, input().split())

sum_move = 0
for i in store_list:
    pass