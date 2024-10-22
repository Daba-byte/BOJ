from collections import deque

def count_water(N, M, bingsan, x, y):  # 빙산 주변 물의 수를 세는 함수
    # 한 칸이라도 붙어있으면 한덩이로 치고, 동서남북으로 다 0이 있어야 분리된다.
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # 방향 바로 들어오고ㅋ
    water = 0  # 주변에 물이 있는지 확인할 변수

    for dx, dy in directions: # 방향 확인하면서
        nx, ny = x + dx, y + dy # 주변 위치가
        if 0 <= nx < N and 0 <= ny < M and bingsan[nx][ny] == 0: # 빙산 안에 있으면서 물이면
            water += 1 # 주변 물 수 올려
    return water # 구한 주변 물 수 반환

def BFS(N, M, bingsan, visited, x, y): # 빙산 덩어리를 세기 위한 bfs
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)] # 방향 또 오고
    queue = deque([(x, y)]) # 내 위치 넣고
    visited[x][y] = 1 # 들렸다 감

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            # 빙산 안에 있으면서 방문 안했고 다 안 녹았을 때
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and bingsan[nx][ny] > 0:
                visited[nx][ny] = 1 # 방문으로 바꾸고
                queue.append((nx, ny)) # 새 위치 넣어

def count_icebergs(N, M, bingsan): # 빙산 덩어리 셀 함수
    visited = [[0] * M for _ in range(N)]
    iceberg_cnt = 0

    for x in range(N): # 빙산
        for y in range(M): # 돌면서
            if bingsan[x][y] > 0 and not visited[x][y]: # 방문 전이면
                BFS(N, M, bingsan, visited, x, y) # bfs 돌려
                iceberg_cnt += 1 # 빙산 덩어리 수
    
    return iceberg_cnt

def melting_iceberg(N, M, bingsan):  # 빙산이 녹는 과정 시뮬레이션 함수
    melting_year = 0  # 분리되는 년도

    while True:
    # 빙산 덩어리 수 세기
        iceberg_count = count_icebergs(N, M, bingsan)
        if iceberg_count >= 2:  # 덩어리가 2개 이상으로 분리되면 종료
            return melting_year # 후후
        if iceberg_count == 0:  # 빙산이 다 녹으면 종료
            return 0 # 분리 안댐

        # 빙산이 녹는 과정
        melt_list = [] # 녹일거야 너네
        for x in range(N):
            for y in range(M):
                if bingsan[x][y] > 0: # 물이 아니면
                    water_count = count_water(N, M, bingsan, x, y) # 주변에 물 가져와서
                    melt_list.append((x, y, water_count)) # 위치랑 주변 물 수 리스트에 넣음

        # 빙산 높이 갱신
        for x, y, water in melt_list: # 녹이는 애들 돌면서
            bingsan[x][y] = max(0, bingsan[x][y] - water) # 녹은 거 버리고 새 높이로 갱신, 다 녹았으면 0으로 갱신 올 ㅋ 나 개천재

        melting_year += 1 # 시간이 지나따

N, M = map(int, input().split())
bingsan = [list(map(int, input().split())) for _ in range(N)]

result = melting_iceberg(N, M, bingsan)
print(result)