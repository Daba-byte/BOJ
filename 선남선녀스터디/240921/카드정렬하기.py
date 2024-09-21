import heapq
import sys

input = sys.stdin.read

def min_comparisons(n, sizes):
    if n == 1:
        return 0
    
    # 최소 힙을 만들기 위한 카드 묶음 넣기
    heapq.heapify(sizes)
    total_comparisons = 0
    
    while len(sizes) > 1:
        # 젤 작은 거 2개
        first = heapq.heappop(sizes)
        second = heapq.heappop(sizes)
        
        # 합치기
        merged_size = first + second
        total_comparisons += merged_size
        
        # 다시 넣기
        heapq.heappush(sizes, merged_size)
    
    return total_comparisons # 비교 회수 계산

data = list(map(int, input().split()))
N = data[0]
sizes = data[1:]

result = min_comparisons(N, sizes)
print(result)


#########################
# 최소힙을 사용
# 가장 작은 묶음 두 개를 꺼내고 크기 합침
# 합친 크기를 다시 힙에 추가
# 합치기 위해 필요한 회수 계산도 같이 하기
# 묶음 하나 남을 떄까지 반복