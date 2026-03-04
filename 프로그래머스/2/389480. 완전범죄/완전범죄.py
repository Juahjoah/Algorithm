def dfs(idx, info, n, m, a, b):
    global answer, visited
    
    if (idx, a, b) in visited:
        return
    visited.add((idx, a, b))
        
    if idx == len(info):
        if a < n and b < m:
            answer = min(answer, a)
        return
    
    if a >= n or b >= m:
        return
    
    # A가 최소보다 커지면 확인할 필요 없음
    if a >= answer:
        return


    # 해당 물건을 a가 훔친 상황
    dfs(idx + 1, info, n, m, a + info[idx][0], b)
    # 해당 물건을 b가 훔친 상황
    dfs(idx + 1, info, n, m, a, b + info[idx][1])
    

def solution(info, n, m):
    global answer, visited
    answer = 10**10
    visited = set()
    
    dfs(0, info, n, m, 0, 0)
    
    if answer == 10**10:
        return -1
    else:
        return answer