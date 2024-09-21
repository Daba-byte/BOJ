from collections import deque

def kevin_law(start, n, graph): # 시작 친구~다른 모든 친구까지 최단거리 계산
    distances = [-1] * (n + 1)
    queue = deque([start])
    distances[start] = 0

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    return sum(distances[1:])  # 1부터 n까지의 거리 합 반환

def find_kevin_bacon(N, M, relations):
    graph = [[] for _ in range(N + 1)]
    
    # 친구 관계 생성
    for a, b in relations:
        graph[a].append(b)
        graph[b].append(a)
    
    # 각 사람들의 케빈 베이컨 수를 계산
    min_bacon = float('inf')
    min_user = 0

    for i in range(1, N + 1):
        bacon = kevin_law(i, N, graph)
        if bacon < min_bacon:
            min_bacon = bacon
            min_user = i
        elif bacon == min_bacon and i < min_user:
            min_user = i
    
    return min_user

N, M = map(int, input().split())
relations = [list(map(int, input().split())) for _ in range(M)]

print(find_kevin_bacon(N, M, relations))