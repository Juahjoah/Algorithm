from collections import deque

def solution(priorities, location):
    answer = 0
    # queue = deque([priorities])
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    
    while queue:
        current = queue.popleft()
        find_queue = False
        
        for q in queue:
            if current[0] < q[0]:
                find_queue = True
                break
                
        if find_queue:
            queue.append(current)
        else:
            answer += 1
            if current[1] == location:
                return answer
    
    return answer