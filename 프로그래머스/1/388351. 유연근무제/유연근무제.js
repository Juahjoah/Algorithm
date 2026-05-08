function solution(schedules, timelogs, startday) {
    let answer = 0;
    
    for (let i = 0; i < schedules.length; i++) {
        // 목표 시간 : 출근 희망 시간 + 10분
        const h = Math.floor(schedules[i] / 100);
        const m = schedules[i] % 100;
        const goalTime = h * 60 + m + 10;
        
        let isPass = true;
        
        for (let j = 0; j < 7; j++) {
            // 현재 요일 계산
            const day = ((startday + j - 1) % 7) + 1;
            
            // 주말은 건너뜀
            if (day >= 6) {
                continue;
            }
            
            const logH = Math.floor(timelogs[i][j] / 100);
            const logM = timelogs[i][j] % 100;
            const checkTime = logH * 60 + logM;
            
            // 탈락 여부 판단
            if (checkTime > goalTime) {
                isPass = false;
                break;
            }
        }
        
        if (isPass) {
            answer++;
        }
    }
    return answer;
}