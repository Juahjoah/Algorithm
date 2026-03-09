def solution(diffs, times, limit):
    left = 1
    right = max(diffs)
    
    while left < right :
        mid = (left + right) // 2
        time = 0
        
        for d in range(len(diffs)):
            diff = diffs[d]
            time_cur = times[d]
            if d > 0:
                time_prev = times[d - 1]
            else:
                time_prev = 0
            
            if diffs[d] <= mid:
                time += time_cur
            else:
                # 퍼즐을 총 diff-level번 틀리게 됨
                fail_cnt = diff - mid
                time += (time_cur + time_prev) * fail_cnt + time_cur
            
            if time > limit:
                break
        
        if time <= limit:
            right = mid
        else:
            left = mid + 1
    
    return left
                