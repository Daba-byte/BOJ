# 못 풀었음.. 런타임 에러..
import sys
input = sys.stdin.read

# 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, 0, 0]

def spread_dust(R, C, board):
    temp = [[0] * C for _ in range(R)] # 확산 저장할 거

    for i in range(R):
        for j in range(C):
            if board[i][j] > 0: # 확산되는 양은?
                spread_amount = board[i][j] // 5
                spread_count = 0

                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]

                    if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != -1:
                        temp[nx][ny] += spread_amount
                        spread_count += 1 # 확산 끝

                # 확산 끝나고 남은 미세먼지
                board[i][j] -= spread_amount * spread_count
    # 확산된 양을 원래 보드에 더하기
    for i in range(R):
        for j in range(C):
            board[i][j] += temp[i][j]


def run_cleaner(R, C, board, cleaner):
    # 시계 방향: 아래쪽
    low = cleaner[1]
    # 반시계 방향: 위쪽
    up = cleaner[0]

    # 시계방향 순환
    for i in range(low+1, R-1):
        board[i][0] = board[i+1][0]
    for i in range(C-1):
        board[R-1][i] = board[R-1][i+1]
    for i in range(R-1, low, -1):
        board[i][C-1] = board[i-1][C-1]
    for i in range(C-1, 1, -1):
        board[low][i] = board[low][i-1]
    board[low][1] = 0 # 공기청정기 공기
    # 와 머리에 쥐날 거 같은데...

    # 반시계 방향 순환... 어우 머리아파 쓰기 싫어
    for i in range(up-1, 0, -1):
        board[i][0] = board[i-1][0]
    for i in range(C-1):
        board[0][i] = board[0][i+1]
    for i in range(C-1, 1, -1):
        board[i][C-1] = board[i+1][C-1]
    for i in range(C-1, 1, -1):
        board[up][i] = board[up][i-1]
    board[up][1] = 0 # 얘도 공기청정기 공기

def micro_dust(R, C, board): # 미세먼지 계산
    total_dust = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                total_dust += board[i][j]
    return total_dust

# data = input().splitlines() # splitlines 처음 써 보는데 좋네 기억하자
R, C, T = map(int, data[0].split())
board = [list(map(int, line.split())) for line in data[1:R+1]]

cleaner = [] # 공기청정기 위치는?
for i in range(R):
    if board[i][0] == -1:
        cleaner.append(i) # 여기다!

# T초 동안 확산, 정화함
for _ in range(T):
    spread_dust(R, C, board) # 확산
    run_cleaner(R, C, board, cleaner) # 정화

result = micro_dust(R, C, board)
print(result)