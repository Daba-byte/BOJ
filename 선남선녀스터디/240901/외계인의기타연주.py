import sys # 시간초과시 넣어보자..

def ding_ga(frets):
    # 각 줄마다 현재 누르고 있는 프렛을 관리할 리스트
    lines = [[] for _ in range(7)]  # 기타는 6줄: 인덱스 1부터 6까지만 쓸거임

    ding_ga_count = 0  # 딩가딩가

    for line, fret in frets:
        # 현재 줄에 프렛이 눌려 있을 때
        while lines[line] and lines[line][-1] > fret:
            lines[line].pop()  # 높은 음 빼고
            ding_ga_count += 1  # 딩가

        # 이미 같은 프렛이 눌러져 있는 경우는 무시
        if lines[line] and lines[line][-1] == fret:
            continue  # 안 딩가

        # 더 높은 프렛을 눌러야 하는 경우
        lines[line].append(fret)  # 높은 음 넣고
        ding_ga_count += 1  # 딩가

    return ding_ga_count  # 총 딩가는?

N, P = map(int, input().split())
frets = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

print(ding_ga(frets))