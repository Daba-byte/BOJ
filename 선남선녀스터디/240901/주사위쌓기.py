def max_dice_num(N, dices):
    # 전개도 상 마주보는 면: A와 F, B와 D, C와 E
    # 이 쌍들의 요소 중 하나가 아래/윗면일 때, 남은 하나가 반드시 아래/위여야 함
    opposite = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0} # 마주보는 면 인덱스

    max_sum = 0 # 가장 큰 옆면의 합은?

    for i in range(6):
        top = dices[0][i] # 첫 주사위의 각 면을 모두 아래로 놓아 볼 때
        current_sum = 0 # 합을 갱신할 값

        # 현재 윗면에 맞춰서 위에 주사위를 놓음
        for dice in dices:
            bottom = top # 위에 쌓을 주사위의 아래 면은 현재 주사위의 윗면 숫자
            top = dice[opposite[dice.index(bottom)]] # 윗면을 다시 위 주사위의 윗면 숫자로 갱신

            # 옆면의 가능한 최대의 숫자를 계산
            sides = {0, 1, 2, 3, 4, 5} # 옆면 인덱스
            sides.remove(dice.index(bottom)) # 아래 제거
            sides.remove(dice.index(top)) # 위 제거

            # 남은 4개의 면 중 가장 큰 값을 더하기
            current_sum += max(dice[j] for j in sides)

        # 자 이제 다왔다 더해보자
        max_sum = max(max_sum, current_sum)

    return max_sum # 그렇게 찾던 최대가 나야

N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]

print(max_dice_num(N, dices))