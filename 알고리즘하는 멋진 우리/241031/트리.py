# 오답임 풀지 못함

import sys
input = sys.stdin.read
from collections import deque

# 니 트리임? 비에프에스
def is_tree(start, graph, visited):
    queue = deque([(start, -1)])
    visited[start] = 1

    while queue:
        current, parent = queue.popleft()

        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                queue.append((neighbor, current))
            elif neighbor != parent:  # 사이클 발견
                return 0
    return 1

def count_trees(n, edges): # 트리 세는 함수
    graph = [] # 하... 못하겠다
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [0] * (n + 1)
    tree_count = 0

    for i in range(1, n + 1):
        if not visited[i] and i in graph:
            if is_tree(i, graph, visited):
                tree_count += 1

    return tree_count

result = []
case_num = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    edges = [list(map(int, input().split())) for _ in range(m)] # ㅠㅠ 못하겠어
    case_num += 1
    tree_count = count_trees(n, edges)

    if tree_count == 0:
        result.append(f"Case {case_num}: No trees.")
    elif tree_count == 1:
        result.append(f"Case {case_num}: There is one tree.")
    else:
        result.append(f"Case {case_num}: A forest of {tree_count} trees.")

print("\n".join(result))