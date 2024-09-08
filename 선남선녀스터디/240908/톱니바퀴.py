from collections import deque

# 톱니바퀴 회전 함수
def rotate(gear, direction):
    if direction == 1:  # 시계 방향
        gear.appendleft(gear.pop())
    elif direction == -1:  # 반시계 방향
        gear.append(gear.popleft())

# 맞닿은 부분 확인
def check_polarity(gear1, gear2, idx1, idx2):
    return gear1[idx1] != gear2[idx2]

gears = [deque(map(int, input().strip())) for _ in range(4)]
K = int(input().strip())
rotations = [tuple(map(int, input().split())) for _ in range(K)]

# 회전 처리
for num, direction in rotations:
    num -= 1  # 인덱스를 0부터 시작하도록 맞춤
    
    # 각 톱니바퀴의 회전 여부와 방향 결정
    rotation_directions = [0] * 4
    rotation_directions[num] = direction
    
    # 왼쪽 톱니바퀴들 확인
    for i in range(num - 1, -1, -1):
        if check_polarity(gears[i], gears[i + 1], 2, 6):
            rotation_directions[i] = -rotation_directions[i + 1]
        else:
            break
    
    # 오른쪽 톱니바퀴들 확인
    for i in range(num + 1, 4):
        if check_polarity(gears[i - 1], gears[i], 2, 6):
            rotation_directions[i] = -rotation_directions[i - 1]
        else:
            break
    
    # 각 톱니바퀴 회전
    for i in range(4):
        if rotation_directions[i] != 0:
            rotate(gears[i], rotation_directions[i])

# 최종 점수는?
score = 0
for i in range(4):
    if gears[i][0] == 1:  # S극일 경우
        score += 2 ** i

print(score)


####################
