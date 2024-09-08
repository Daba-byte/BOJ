# 야구는 엘지..
# 이거도 못품.. 시간초과...
from itertools import permutations

def play_game(order, innings):
    score = 0
    hitter_idx = 0
    
    for inning in innings:
        bases = [0, 0, 0]  # 1루, 2루, 3루
        out_count = 0
        
        while out_count < 3:
            result = inning[order[hitter_idx]]
            
            if result == 0:  # 아웃
                out_count += 1
            elif result == 1:  # 안타
                score += bases[2]  # 3루에 있는 주자는 득점
                bases = [1, bases[0], bases[1]]  # 주자들이 진루
            elif result == 2:  # 2루타
                score += bases[2] + bases[1]  # 3루, 2루에 있는 주자는 득점
                bases = [0, 1, bases[0]]  # 주자들이 진루
            elif result == 3:  # 3루타
                score += bases[2] + bases[1] + bases[0]  # 모든 주자가 득점
                bases = [0, 0, 1]  # 타자는 3루로 이동
            elif result == 4:  # 홈런
                score += bases[2] + bases[1] + bases[0] + 1  # 모든 주자 + 타자가 득점
                bases = [0, 0, 0]  # 모든 주자는 홈으로 이동
                
            # 다음 타자로 순서를 넘김
            hitter_idx = (hitter_idx + 1) % 9
            
    return score

n = int(input())
innings = [list(map(int, input().split())) for _ in range(n)]

# 1번 선수는 4번 타자로 고정되기 때문에 이를 제외한 나머지 8명의 순서를 순열로 배치
max_score = 0
for order in permutations(range(1, 9)):
    # 4번 타자는 1번 선수로 고정
    current_order = list(order[:3]) + [0] + list(order[3:])
    
    # 해당 타순으로 게임을 시뮬레이션
    score = play_game(current_order, innings)
    max_score = max(max_score, score)

print(max_score)