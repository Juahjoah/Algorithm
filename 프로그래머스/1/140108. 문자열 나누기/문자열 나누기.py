def solution(s):
    answer = 0
    answer_list = []
    cnt_x = 0
    cnt_y = 0
    x = " "
    
    for i in range(len(s)):
        if x == " ":
            x = s[i]
        
        if s[i] == x:
            cnt_x += 1
        else:
            cnt_y += 1

        if cnt_x == cnt_y:
            answer += 1
            x = " "
            cnt_x = 0
            cnt_y = 0
    
    if cnt_x != 0 or cnt_y != 0:
        answer += 1

    return answer