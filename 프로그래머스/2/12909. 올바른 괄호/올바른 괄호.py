def solution(s):
    answer = True
    stack = []
    
    for s in s:
        if s == '(':
            stack.append(s)
        else:
            if stack:
                stack.pop()
            else:
                answer = False
                break
                    
    if stack:
        answer = False
    
    return answer