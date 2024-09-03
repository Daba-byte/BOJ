def calculate_city_chicken_distance(houses, selected_chickens): # 치킨 거리 계산하고 반환하기
    total_distance = 0 # 인자 넣으면 거리를 알려주마
    for house_r, house_c in houses: # 집 좌표 내놔
        min_distance = float('inf') # 각 집에 대해 치킨집과 거리를 저장할 변수
        for chicken_r, chicken_c in selected_chickens: # 치킨 집 좌표도 내놔
            distance = abs(house_r - chicken_r) + abs(house_c - chicken_c) # 그 치킨집이랑 그 집은 이정도 거리다
            min_distance = min(min_distance, distance) # 근데 더 가까운 치킨집은 여기다
        total_distance += min_distance # 그래서 이 치킨 거리는
    return total_distance # 이 정도야

# 셀렉 리스트 안에 선택된 치킨집 저장할 거임
# 그리고 치킨집 M개 선택되면, 치킨 거리 계산
def backtrack(index, selected_chickens, houses, chicken_store, M):
    # 현재 치킨집을 선택할 인덱스, 현재 선택된 치킨집 리스트, 집 위치, 치킨집 위치, 선택 치킨집 수
    global min_city_chicken_distance # 구해야 하는 값
    
    # M개의 치킨집을 선택했다면 도시의 치킨 거리를 계산
    if len(selected_chickens) == M: # 만약 이미 M개의 치킨집이 선택 되었다면
        current_distance = calculate_city_chicken_distance(houses, selected_chickens) # 현재 선택된 치킨집으로 치킨 거리 계산
        min_city_chicken_distance = min(min_city_chicken_distance, current_distance) # 최소 값인지 비교
        return # 내가 젤 작아 여기야 여기
    
    # 치킨집을 선택하는 백트래킹
    for i in range(index, len(chicken_store)): # 선택되지 않은 치킨집 중
        selected_chickens.append(chicken_store[i]) # 하나를 선택 후
        backtrack(i + 1, selected_chickens, houses, chicken_store, M) # 재귀 호출로 다음 집 선택
        selected_chickens.pop()  # 선택 해제 (백트래킹): 마지막에 선택된 치킨집을 제거하여, 이전 상태로 돌아가기

def chicken_distance(N, M, city): # 치킨 거리를 구하자
    houses = [] # 집 위치 저장: (r, c)
    chicken_store = [] # 치킨집 저장: (r, c)
    
    # 도시에서 집과 치킨집의 위치를 파악
    for r in range(N): # 도시 돌아
        for c in range(N): # 돌아 돌아
            if city[r][c] == 1: # 좌표 위치가 1이면
                houses.append((r, c)) # 그건 집이야
            elif city[r][c] == 2: # 2면
                chicken_store.append((r, c)) # 그건 치킨 집이야
    
    # 전역 변수로 최소 치킨 거리 선언
    global min_city_chicken_distance # 아무래도 값 다 저장하고 작은 값으로 갱신해야하니까
    min_city_chicken_distance = float('inf') # 무한으로 해줄게
    
    # 백트래킹 시작. 난 백트래킹 재미는 있는데 싫어
    # 벗 즐거워 하웨버 머리아파
    # 진짜 내 마음은 몰까...
    backtrack(0, [], houses, chicken_store, M) # 자 이제 백트레킹 함수에서 무슨 일이 일어나는 지 보자
    
    return min_city_chicken_distance # 최소 거리 나야 나

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

print(chicken_distance(N, M, city))