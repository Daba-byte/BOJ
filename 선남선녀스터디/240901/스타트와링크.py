# 이거 재귀로 풀어야 하나보네 너무 싫다..
def min_attribute_gap(N, grid):
    min_diff = [float('inf')]  # 결과 저장용 (최소 차이를 저장)
    backtrack(0, [], [], N, grid, min_diff) # 백트래킹 함수 넣어
    return min_diff[0] # 가장 처음 값이 최소 차이

def calculate_team_score(team, grid):
    # 주어진 팀의 능력치를 계산
    score = 0 # 능력치
    team_size = len(team) # 몇 명이냐
    for i in range(team_size): # 인원수만큼 돌아
        for j in range(i + 1, team_size): # 돌아 돌아
            score += grid[team[i]][team[j]] + grid[team[j]][team[i]]
    return score # 능력치 반환

def backtrack(index, start_team, link_team, N, grid, min_diff):
    # 모든 사람을 팀에 배치했을 때
    if index == N: # 모든 사람이(0부터 N-1까지) 팀에 배정됨
        # 두 팀의 능력치를 계산
        start_score = calculate_team_score(start_team, grid) # 스타트팀 능력치
        link_score = calculate_team_score(link_team, grid) # 링크팀 능력치
        # 능력치 차이의 최소값 갱신
        diff = abs(start_score - link_score) # 능력치 차이
        min_diff[0] = min(min_diff[0], diff) # 젤 작은 건 누구냐!
        return # 나다

    # 사람들을 어떻게 배치해서 더할 것인가?
    # 인덱스 돌면서 현재 들어간 팀의 크기가 전체 크기 절반 보다 작은 경우에 추가할 것
    # 이러면 두팀이 절반으로 나눠짐

    # 현재 사람을 스타트 팀에 추가하는 경우
    if len(start_team) < N // 2:
        start_team.append(index)  # 현재 사람을 스타트 팀에 추가
        backtrack(index + 1, start_team, link_team, N, grid, min_diff)  # 다음 사람으로 넘어감
        start_team.pop()  # 백트래킹: 팀에 추가했던 현재 사람을 다시 제거

    # 현재 사람을 링크 팀에 추가하는 경우
    if len(link_team) < N // 2:
        link_team.append(index)  # 현재 사람을 링크 팀에 추가
        backtrack(index + 1, start_team, link_team, N, grid, min_diff)  # 다음 사람으로 넘어감
        link_team.pop()  # 백트래킹: 팀에 추가했던 현재 사람을 다시 제거

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

result = min_attribute_gap(N, grid)
print(result)