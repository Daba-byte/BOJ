# 문제의 포인트는 테트로미노 어쩌구에 꽂히면 안됨.
# 걍 붙어있는 4개 가려서 젤 큰수 구하는 거임
# 은 할 줄 몰라서 좌표 다 씀 ㅋㅋㅋ
# 은 그래도 틀림 왜 안돌아가냐 저혈압 완치

# 테트로미노 모양 좌표 정의하긴 해야함
# 개귀찮네 진짜
tetromino_shapes = [
    # 막대 모양 (I자)
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # 가로로 놓인 막대
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # 세로로 놓인 막대

    # 정사각형 모양 (ㅁ자)
    [(0, 0), (0, 1), (1, 0), (1, 1)],  # 정사각형

    # L자 모양 (L자)
    [(0, 0), (1, 0), (2, 0), (2, 1)],  # 'L' 모양
    [(0, 1), (1, 1), (2, 1), (2, 0)],  # 'ㄱ' 모양 (L의 대칭)
    [(0, 0), (0, 1), (0, 2), (1, 0)],  # 눕힌 'ㄴ' 모양
    [(0, 0), (0, 1), (0, 2), (1, 2)],  # 눕힌 'ㄱ' 모양

    # Z자 모양 (Z자)
    [(0, 0), (0, 1), (1, 1), (1, 2)],  # 'Z' 모양
    [(0, 1), (1, 0), (1, 1), (2, 0)],  # 반대 'Z' 모양

    # ㅗ자 모양 (T자)
    [(0, 1), (1, 0), (1, 1), (1, 2)],  # 'ㅗ' 모양
    [(1, 0), (0, 1), (1, 1), (2, 1)],  # 'ㅓ' 모양
    [(1, 0), (1, 1), (1, 2), (0, 1)],  # 'ㅜ' 모양
    [(1, 0), (0, 1), (1, 1), (2, 1)]   # 'ㅏ' 모양
]
# 다 쓰고 나서 느낀점: 이게 맞나.. 분명 더 쉬운 방법이 있을 거 같은데..

def tetromino(N, M, paper):
    max_sum = 0 # 최대 값
    
    for i in range(N): # 종이 안에서
        for j in range(M):
            for shape in tetromino_shapes: # 좌표 돌면서
                current_sum = 0 # 합 저장
                valid = True # 테트로미노 일부가 종이를 벗어나지 않는지 확인
                for dx, dy in shape:
                    x, y = i + dx, j + dy
                    if 0 <= x < N and 0 <= y < M: # x, y가 종이 안에 있으면
                        current_sum += paper[x][y] # 더해
                    else: # 범위 벗어나면
                        valid = False # 넌 아니야
                        break # 멈춰
                if valid: # valid가 여전히 True라면
                    max_sum = max(max_sum, current_sum) # 최댓값 구해줘
    return max_sum # 구랭

N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

print(tetromino(N, M, paper))