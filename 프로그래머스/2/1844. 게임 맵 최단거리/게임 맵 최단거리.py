from collections import deque

def solution(maps):
    answer = -1
    n = len(maps[0])
    m = len(maps)
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    visited = [[0] * n for _ in range(m)]
    queue = deque([(0, 0, 1)])
    visited[0][0] = 1
    
    while queue:
        x, y, cnt = queue.popleft()
        
        if x == m - 1 and y == n - 1:
            return cnt      
        
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0 and maps[nx][ny] == 1:
                visited[nx][ny] = 1
                queue.append((nx, ny, cnt + 1))
                
    return answer