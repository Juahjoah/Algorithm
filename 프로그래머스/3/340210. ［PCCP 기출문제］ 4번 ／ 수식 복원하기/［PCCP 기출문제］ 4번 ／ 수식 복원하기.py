# 각 진법으로 변환하기
def to_base(num, base):
    if num == 0:
        return '0'
        
    result = ''
    while num > 0:
        result = str(num % base) + result
        num //= base
    return result
        
def solution(expressions):
    # 가능한 모든 진법 찾기
    valid_bases = []
    
        
    # 최대 진법 찾기
    max_digit = 0
    for exp in expressions:
        for token in exp.split():
            if token.isdigit():
                for ch in token:
                    max_digit = max(max_digit, int(ch))
    
    
    for base in range(max_digit + 1, 10):
        flag = True
        
        for exp in expressions:
            A, op, B, _, C = exp.split()
        
            if C == 'X':
                continue
            
            try:
                a = int(A, base)
                b = int(B, base)
                c = int(C, base)
            except:
                flag = False
                break
            
            if op == '+':
                if a + b != c:
                    flag = False
                    break
            else:
                if a - b != c:
                    flag = False
                    break
                    
        if flag:
            valid_bases.append(base)

    
    # 그 진법에 맞춰 정답 확인하기
    answer = []
    for exp in expressions: 
        A, op, B, _, C = exp.split()
        
        possible = set()
        
        if C != 'X':
            continue
        for base in valid_bases:
            try:
                a = int(A, base)
                b = int(B, base)
                
                if op == '+':
                    res = a + b
                else:
                    res = a - b
                
                possible.add(to_base(res, base))
            except:
                continue
    
        if len(possible) == 1:
            val = possible.pop()
        else:
            val = '?'

        answer.append(f"{A} {op} {B} = {val}")        
            
    return answer