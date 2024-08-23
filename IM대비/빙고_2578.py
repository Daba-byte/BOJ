def bingo_check(board):
    sum_line = 0
    # 가로
    for row in board:
        if all(x == 0 for x in row):
            sum_line += 1

    # 세로
    for col in range(5):
        if all(board[row][col] == 0 for row in range(5)):
            sum_line += 1
    
    # 대각선 왼->오
    if all(board[i][i] == 0 for i in range(5)):
        sum_line += 1

    # 대각선 오->왼
    if all(board[i][4 - i] == 0 for i in range(5)):
        sum_line += 1

    return sum_line

def bingo(cheol, ans):
    board = [row[:] for row in cheol] # 게임보드 초기화
    step = 0

    for num in ans:
        step += 1
        for i in range(5):
            for j in range(5):
                if board[i][j] == num:
                    board[i][j] = 0
                    break

        if bingo_check(board) >= 3:
            return step
        
    return None

cheolsu_bingo = [list(map(int, input().split())) for _ in range(5)]
remove = []
for _ in range(5):
    remove += list(map(int, input().split()))

result = bingo(cheolsu_bingo, remove)
print(result)