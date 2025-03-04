from collections import deque

def solution(land):
        
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    oil_id = 2              # land 기본값이 1이니까 2부터 시작
    oil_size = {}
    
    # visited 처리해줌과 동시에 land 값에 연결되어 있는 칸의 수를 세서 집어넣기 -> 불가
    # 연결된 칸의 수는 id 값으로 연결해 딕셔너리에 저장하고, land에는 id 값을 저장
    def BFS(i, j):
        queue = deque()
        queue.append((i, j))
        
        visited[i][j] = True
        cnt = 1 #시작하는 칸 포함
        
        position = [(i, j)]
        
        while queue:
            x, y = queue.popleft()
            
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and land[nx][ny] == 1:
                    visited[nx][ny] = True
                    cnt += 1
                    queue.append((nx, ny))
                    position.append((nx, ny))
        
        for x, y in position:
            land[x][y] = oil_id
        
        oil_size[oil_id] = cnt

        return cnt
                    
    # n, m 값 세기
    n = len(land)
    m = len(land[0]) if land else 0
    # while True:
    #     for checklands in land:
    #         n += 1
    #         for checkland in checklands:
    #             if not m:
    #                 m += 1
    #     break
        
    visited = [[False]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                BFS(i, j)
                oil_id += 1
    
    # 각 열마다 나오는 값 중 최고 값을 골라서 반환
    answer_list = []
    
    # oil_id가 중복되지 않는 경우만 찾아야 함
    for k in range(m):
        count = 0
        oil_list = []
        for j in range(n):
            oil_id = land[j][k]
            if oil_id >= 2 and oil_id not in oil_list:
                count += oil_size[oil_id]
                oil_list.append(oil_id)
                
        answer_list.append(count)
    
    return max(answer_list)