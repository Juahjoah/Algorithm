def solution(schedules, timelogs, startday):
    answer = 0

    for i in range(len(schedules)):
        h = schedules[i] // 100
        m = schedules[i] % 100
        goaltime = (h * 60) + m + 10
        timelog = timelogs[i]
        
        cnt = 0
        day = startday
        for j in range(7):
            now = day % 7
            
            if now == 6 or now == 0:
                day += 1
                continue
            else:
                h = timelog[j] // 100
                m = timelog[j] % 100
                checktime = (h * 60) + m 
                
                if checktime <= goaltime:
                    cnt += 1
                else:
                    break
                    
            if cnt == 5:
                answer += 1 
            day += 1
                           
    return answer