def solution(wallet, bill):
    answer = 0
    
    while max(wallet) < max(bill) or min(wallet) < min(bill):
        # 길이가 긴 쪽을 접기
        if bill[0] > bill[1]:
            bill[0] = bill[0] // 2
        else:
            bill[1] = bill[1] // 2
        answer += 1
    
    return answer