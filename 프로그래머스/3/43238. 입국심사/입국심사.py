def solution(n, times):
    answer = 0
    
    start = 0
    end = max(times) * n
    
    while start <= end:
        # mid = mid 시간 동안 처리할 수 있는 사람
        mid = (start + end) // 2
        total = 0
        
        for t in times:
            # total = 감당할 수 있는 사람 수
            total += mid // t
            # 심사해야 하는 인원보다 많아졌을 때 break
            if total >= n:
                break
                
        if total >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
            
    return answer