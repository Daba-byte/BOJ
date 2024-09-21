from collections import deque

# 방문 처리하는 함수 bfs 사용
def baechu_nyam(bat, x, y, M, N):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    queue = deque([(x, y)])
    bat[x][y] = 0

    while queue:
        cx, cy = queue.popleft()        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < M and bat[nx][ny] == 1:
                bat[nx][ny] = 0 # 들렸다
                queue.append((nx, ny))

# 배추흰지렁이 수는?
def like_baechu(M, N, K, baechu):
    bat = [[0] * M for _ in range(N)]  # N x M 크기 배열 초기화

    for x, y in baechu:
        bat[y][x] = 1  # 좌표에 맞게 값 설정안해서 계속 틀림.. x가 열, y가 행

    jireongi = 0

    for i in range(N):
        for j in range(M):
            if bat[i][j] == 1: # 배추 발견
                baechu_nyam(bat, i, j, M, N)
                jireongi += 1

    return jireongi

T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    baechu = []
    for _ in range(K):
        X, Y = map(int, input().split())
        baechu.append((X, Y))

    result = like_baechu(M, N, K, baechu)
    print(result)