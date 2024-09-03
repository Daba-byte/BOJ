def whos_win(omock):
    # 방향 벡터: 가로, 세로, 대각선 2가지
    # 난 벡터가 정말 싫어
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
    
    for i in range(19):
        for j in range(19):
            if omock[i][j] != 0:  # 빈 칸이 아닌 경우
                current_color = omock[i][j]

                for dx, dy in directions:  # 네 방향에 대해 탐색
                    cnt = 1  # 현재 위치 포함

                    # 5개까지 연속된지 체크
                    for step in range(1, 5): # 현재 위치부터 5개까지
                        nx, ny = i + dx * step, j + dy * step
                        # 범위 내에서 색이 같다면
                        if 0 <= nx < 19 and 0 <= ny < 19 and omock[nx][ny] == current_color:
                            cnt += 1 # 카운트 올려
                        else: # 없으면
                            break # 멈춰

                    # 5개 연속된 경우, 6개 연속되지 않도록 체크
                    if cnt == 5:
                        # 양쪽 끝이 같은 색인지 체크
                        if 0 <= i - dx < 19 and 0 <= j - dy < 19 and omock[i - dx][j - dy] == current_color:
                            continue
                        if 0 <= i + dx * 5 < 19 and 0 <= j + dy * 5 < 19 and omock[i + dx * 5][j + dy * 5] == current_color:
                            continue
                        # 승리한 경우
                        return current_color, i + 1, j + 1

    # 승리자가 없는 경우
    return 0

omock = [list(map(int, input().split())) for _ in range(19)]
result = whos_win(omock)

if result == 0:
    print(0)
else:
    print(result[0])
    print(result[1], result[2])