from collections import deque 

def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n + 1)]
    visited = [-1] * (n + 1)
    
    for s, a in edge:
        graph[s].append(a)
        graph[a].append(s)
    
    # 탐색을 시작할 노드 (1번 노드)에 대한 정보 저장
    queue = deque([1])
    visited[1] = 0          # 1번 노드의 거리는 무조건 0 (본인이니까)
    
    # BFS로 탐색
    while queue:
        now = queue.popleft()
        
        for next in graph[now]:
            if visited[next] == -1:      # 방문하지 않았다면,
                queue.append(next)
                visited[next] = visited[now] + 1
                
    max_visited = max(visited)
    for v in visited:
        if v == max_visited:
            answer += 1
    
    return answer