from datetime import datetime

def solution(today, terms, privacies):
    answer = []
    
    y, m, d = map(int, today.split("."))
    now = y * 12 * 28 + m * 28 + d
    
    # 약관별 기간 저장
    terms_dic = dict()
    for term in terms:
        type, period = term.split(" ")
        terms_dic.update({type : int(period)})
    
    # 날짜와 약관 번호 분류
    for idx, privacy in enumerate(privacies):
        day, type = privacy.split(" ")
        
        # 날짜 
        y, m, d = map(int, day.split("."))
        start_day = y * 12 * 28 + m * 28 + d
        expire_day = start_day + terms_dic[type] * 28 - 1           # 오늘을 빼야하기 때문에 -1
        
        # 두 값을 비교
        if now > expire_day:
            answer.append(idx + 1)

    return answer