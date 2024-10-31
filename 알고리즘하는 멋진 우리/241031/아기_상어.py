from collections import deque

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

# 아기 상어 초기 설정하기
shark_size = 2 # 애기 상어 크기
shark_eat_count = 0
shark_x, shark_y = 0, 0

# 아기 상어 위치 찾기
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            shark_x, shark_y = i, j
            space[i][j] = 0  # 상어 위치

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS를 사용하여 최단 거리 물고기 탐색하는 함수
def bfs(shark_x, shark_y, shark_size):
    visited = [[0] * N for _ in range(N)]
    queue = deque([(shark_x, shark_y, 0)])
    visited[shark_x][shark_y] = 1
    fish_list = []
    min_dist = float('inf')
    
    while queue:
        x, y, dist = queue.popleft()
        
        # 물고기 발견 조건
        if 0 < space[x][y] < shark_size: # 상어 사이즈보다 작니
            if dist < min_dist:
                min_dist = dist
                fish_list = [(x, y, dist)]
            elif dist == min_dist:
                fish_list.append((x, y, dist))
        
        # BFS 탐색 흐흐
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if space[nx][ny] <= shark_size:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, dist + 1))
    
    # 가장 위쪽, 가장 왼쪽의 물고기 선택
    if fish_list:
        fish_list.sort()  # (x, y, dist) 기준으로 정렬
        return fish_list[0]
    else:
        return None

# 아기 상어의 전체 이동 시간
total_time = 0

# 먹이 찾기
while True:
    result = bfs(shark_x, shark_y, shark_size)
    if result is None:  # 더 이상 먹을 수 있는 물고기가 없을 때 끝
        break
    fish_x, fish_y, dist = result
    
    # 아기 상어 이동 및 시간 추가
    shark_x, shark_y = fish_x, fish_y
    total_time += dist
    
    # 물고기 내놔
    space[fish_x][fish_y] = 0
    shark_eat_count += 1 # 맛잇다
    
    # 아기 상어 크기 증가
    if shark_eat_count == shark_size: # 사이즈만큼 머그면
        shark_size += 1 # 커져
        shark_eat_count = 0 # 배고파짐

print(total_time)