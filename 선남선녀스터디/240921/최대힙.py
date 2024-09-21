# 최소힙이랑 똑같어 걍 부호 차이
import heapq
import sys

input = sys.stdin.read

def process_commands(commands):
    max_heap = []
    result = []
    
    for command in commands:
        if command > 0:
            heapq.heappush(max_heap, -command)  # 최대 힙잉꼐 음수로
        elif command == 0:
            if max_heap:
                result.append(-heapq.heappop(max_heap))  # 꺼낸 값을 다시 양수
            else:
                result.append(0)
    
    return result

data = list(map(int, input().split()))
N = data[0]
commands = data[1:]

output = process_commands(commands)
sys.stdout.write("\n".join(map(str, output)) + "\n")