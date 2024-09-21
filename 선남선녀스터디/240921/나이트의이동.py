from collections import deque

def move_knight(N, r1, c1, r2, c2):
    directions = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-2, -1), (-1, -2)]

    visited = [[0] * N for _ in range(N)]
    queue = deque([(r1, c1, 0)]) # 0은 이동 횟수
    visited[r1][c1] = 1

    while queue:
        r, c, moves = queue.popleft()

        if r == r2 and c == c2: # 원하는 위치에 도차갛면
            return moves
        
        for dr, dc in directions: # 이동 가능한지 8방향 췤
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = 1
                queue.append((nr, nc, moves + 1))

    return -1 # 도달 불가 경우는 없는 듯

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    result = move_knight(N, r1, c1, r2, c2)
    print(result)