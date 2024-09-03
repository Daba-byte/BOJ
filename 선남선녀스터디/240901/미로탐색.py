# IM도 못 땃는데 BFS라니 진짜 좀 봐주라 ㅠ
from collections import deque # 덱 들어와 디졌다

def bfs(maze, N, M):
    # 상, 하, 좌, 우
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # BFS를 위한 큐 초기화: 시작점 (0, 0)
    queue = deque([(0, 0)])
    
    # BFS 실행한다 드루와
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치에서 네 방향으로 이동 가능한지 확인
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 미로 범위 내에 있고, 이동할 수 있는 칸(1)인지 확인
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                # 새로운 칸으로 이동하며 거리 증가
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    
    # 최종 목적지 (N-1, M-1)까지의 최소 거리는?
    return maze[N-1][M-1] # 나다!

N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

print(bfs(maze, N, M))