from collections import deque

def bfs(target, storage, n, m):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
        
    visited = list([0] * (m + 2) for _ in range(n + 2))
    new_storage = list([0] * (m + 2) for _ in range(n + 2))
    for i in range(n):
        for j in range(m):
            new_storage[i+1][j+1] = storage[i][j]

    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if not (0 <= nx < n + 2 and 0 <= ny < m + 2):
                continue
            if visited[nx][ny] == 1:
                continue
                
            visited[nx][ny] = 1
            
            if new_storage[nx][ny] == target:
                new_storage[nx][ny] = 0
            elif new_storage[nx][ny] == 0:
                queue.append((nx, ny))
        
    for i in range(n):
        for j in range(m):
            storage[i][j] = new_storage[i+1][j+1]


def solution(storage, requests):
    answer = 0
    storage = [list(s) for s in storage]
    n = len(storage) # rows 
    m = len(storage[0]) # cols
            
    for request in requests:        
        if len(request) == 1:
            # 지게차로 꺼내는 경우
            bfs(request[0], storage, n, m)
        else:
            # 크레인으로 꺼내는 경우
            for rows in range(n):   
                for cols in range(m):
                    if storage[rows][cols] == request[0]:
                        storage[rows][cols] = 0
                        
    for r in range(n):
        for c in range(m):
            if storage[r][c]!= 0:
                answer += 1
    
    return answer