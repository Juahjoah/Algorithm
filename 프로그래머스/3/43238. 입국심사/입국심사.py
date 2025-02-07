def solution(n, times):
    left = 0
    right = max(times) * n
    
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        
        # mid 시간 동안 처리할 수 있는 사람
        total_time = 0
        for t in times:
            total_time += mid // t
            # n을 초과했다면 중지
            if total_time >= n:
                break
                
        if total_time >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer