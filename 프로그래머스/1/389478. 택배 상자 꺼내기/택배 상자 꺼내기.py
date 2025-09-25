def solution(n, w, num):
    answer = 0
    
    box_list = []
    flag_box_list = []
    flag = True
    for i in range(1, n+1):
        flag_box_list.append(i)
        if len(flag_box_list) == w:
            if not flag: 
                flag_box_list.reverse()

            box_list.append(flag_box_list)
            flag = not flag
            flag_box_list = []
    
    # 마지막 줄이 w개 미만으로 남았을 때 
    if flag_box_list:
        list_length = len(flag_box_list)
        if flag:
            flag_box_list.extend([0] * (w - list_length))
            box_list.append(flag_box_list)
        else:
            flag_box_list.reverse()
            final_row = [0] * (w - list_length) + flag_box_list
            box_list.append(final_row)
        
    print(box_list)
    
    # 인덱스 값 찾기
    i = j = 0
    for r, row in enumerate(box_list):
        if num in row:
            i = r
            j = row.index(num)
            break
            
    for r in range(i, len(box_list)):
        if box_list[r][j] != 0:
            answer += 1
            
    return answer