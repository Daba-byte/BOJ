def bitmul(H, W, blocks):
    # 블럭은 1로 바꿈
    grid = [[0] * W for _ in range(H)] # 0으로 2차원 세상 만들고
    for i in range(W):
        num = 0
        for j in range(H-1, -1, -1):
            if num < blocks[i]: # blocks 숫자까지
                grid[j][i] = 1 # 1로 기둥 세움
                num += 1

    rainwater = 0 # 빗물
    for i in range(H):
        left = -1 # 왼쪽 벽 인덱스
        for j in range(W):
            if grid[i][j] == 1: # 벽을 만나면
                if left == -1: # 첫 번째 벽일 때
                    left = j # 다음 벽으로 바꿔
                else:
                    for k in range(left + 1, j):
                        if grid[i][k] == 0:
                            grid[i][k] = 2 # 사이 값 2로 바꾸고
                            rainwater += 1 # 빗물 추가
                    left = j # 왼쪽 벽 다시 갱신

    return rainwater # 쌓인 빗물의 수
                     
H, W = map(int, input().split()) # 2차원 세상 높이, 넓이
blocks = list(map(int, input().split())) # 2차원 세상에서의 블록 리스트

result = bitmul(H, W, blocks)
print(result)