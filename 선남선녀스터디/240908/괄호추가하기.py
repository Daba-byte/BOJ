def calculate(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

def solve(index, current_result):
    global max_result
    
    # 수식의 끝까지 도달한 경우
    if index == len(operators):
        max_result = max(max_result, current_result)
        return
    
    # 괄호 없이 다음 연산 처리
    next_result = calculate(current_result, operators[index], numbers[index + 1])
    solve(index + 1, next_result)
    
    # 괄호로 다음 연산 처리 (index + 2가 범위를 넘지 않도록 확인)
    if index + 1 < len(operators):
        bracket_result = calculate(numbers[index + 1], operators[index + 1], numbers[index + 2])
        next_result_with_bracket = calculate(current_result, operators[index], bracket_result)
        solve(index + 2, next_result_with_bracket)

N = int(input())
expression = input()

# 숫자와 연산자 분리
numbers = []
operators = []
for i in range(N):
    if i % 2 == 0:
        numbers.append(int(expression[i]))
    else:
        operators.append(expression[i])

# 결과값 변수 초기화
max_result = -2**31  # 주어진 범위에 맞는 초기 최소값 설정

# 재귀적으로 문제 해결 시작 (첫 번째 숫자부터 시작)
solve(0, numbers[0])

print(max_result)