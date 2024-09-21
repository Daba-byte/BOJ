import heapq # 리스트를 최소 힙으로 다루게 해줌. 힙푸쉬랑 팝
import sys

input = sys.stdin.read

def process_commands(commands):
    min_heap = []
    result = []
    
    for command in commands:
        if command > 0:
            heapq.heappush(min_heap, command)
        elif command == 0:
            if min_heap:
                result.append(heapq.heappop(min_heap))
            else:
                result.append(0)
    
    return result

data = list(map(int, input().split()))
N = data[0]
commands = data[1:]

output = process_commands(commands)
# 시간초과 안나는 법이라고 동연오빠가 알려줬는데 뭔 말인지 아직도 모름
sys.stdout.write("\n".join(map(str, output)) + "\n") 