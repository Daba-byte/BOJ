#################

# 피보나치 수열 검색
def fibo(N):
    a, b = 1, 1
    if N == 1 or N == 2:
        return 1
    for _ in range(1, N):
        a, b = b, a + b
        return a
    
################
# 가장 긴 수열을 가지는 값을 찾기 위한 함수
def find_max_sequence(first_number): # first_number는 첫 번째 값
    max_length = 0 # 길이
    best_sequence = [] # 짱 긴 리스트

    for second_number in range(1, first_number + 1): # 1부터 큰 값까지
        sequence = [first_number, second_number] # 일단 얘네 넣어
        while True: # 와일 돌려
            next_number = sequence[-2] - sequence[-1] # 다음 숫자부터는 앞앞 - 앞 으로 결정
            if next_number < 0: # 만약 음수가 되면
                break # 멈춰
            sequence.append(next_number) # 음수 아닌 숫자 넣고

        if len(sequence) > max_length: # 젤 긴 수열 찾기
            max_length = len(sequence) # 짜안 나야
            best_sequence = sequence # 그리고 젤 긴게 짱이야

    return max_length, best_sequence # 길이랑 리스트 반환

first_number = int(input())
max_len, best = find_max_sequence(first_number)

print(max_len)
print(' '.join(map(str, best))) # str로 받기.. int 차별하네 ㅠㅠ