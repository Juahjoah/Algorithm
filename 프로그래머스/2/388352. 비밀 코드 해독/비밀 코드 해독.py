from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    
    for check in combinations(range(1, n + 1), 5):
        check_flag = True

        
        for i in range(len(q)):        
            '''
            cnt = 0
            for num in check:
                if num in q[i]:
                    cnt += 1
            '''
            cnt = len(set(check) & set(q[i]))
            if cnt != ans[i]:
                check_flag = False
                break
            
        if check_flag:
            answer += 1
    
    return answer