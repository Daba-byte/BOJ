def find_max_tem(N, K, temperatures):
    # 첫 번째 K일 동안의 합
    max_tem = sum(temperatures[:K]) # K일의 온도 합 중 가장 큰 값. 최대를 유지.
    current_sum = max_tem # 현재 연속적인 K일 동안 합. 매번 갱신됨.

    for i in range(1, N - K + 1):
        # 한 칸씩 옮기면서 연속적인 K값을 갱신하는 구양
        current_sum = current_sum - temperatures[i - 1] + temperatures[i + K -1]
        max_tem = max(max_tem, current_sum) # 야 누가 더 크냐

    return max_tem # 저요

N, K = map(int, input().split())
temperatures = list(map(int, input().split()))

result = find_max_tem(N, K, temperatures)
print(result)