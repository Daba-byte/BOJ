def self_num(n): # 숫자 n에 대해 각 자리수 합 더하기
    result = n
    while n > 0:
        result += n % 10
        n //= 10
    return result

def find_self_numbers(limit): # 리미트가 10000인 문제긴 함
    generated = set()
    
    for i in range(1, limit + 1):
        generated.add(self_num(i)) #집합에 추가
    
    for i in range(1, limit + 1):
        if i not in generated: # 포함 안되는 숫자들
            print(i)

# 10000까지의 셀프 넘버 출력
find_self_numbers(10000)