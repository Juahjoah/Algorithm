from collections import defaultdict, deque

def solution(nodes, edges):
    # 1. 인접 리스트(그래프) 구성
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = set()
    hol_jjak_trees = 0
    reverse_hol_jjak_trees = 0

    # 2. 모든 노드를 돌면서 연결 요소(트리) 단위로 탐색
    for start_node in nodes:
        if start_node in visited:
            continue
        
        # 새로운 트리(컴포넌트) 탐색 시작
        queue = deque([start_node])
        visited.add(start_node)
        
        hol_jjak_match = 0     # 루트가 아닐 때 [홀짝] 조건 만족하는 노드 수
        reverse_match = 0      # 루트가 아닐 때 [역홀짝] 조건 만족하는 노드 수
        
        while queue:
            curr = queue.popleft()
            
            node_parity = curr % 2
            # 루트가 아닐 때의 자식 수 = (전체 연결 간선 수 - 1)
            # 단, 노드가 1개만 홀로 존재하는 트리의 경우 차수가 0이 될 수 있음
            degree = len(graph[curr])
            child_count_if_not_root = degree - 1
            
            # 홀짝 조건 판별: (노드 번호 홀짝) == (자식 수 홀짝)
            if node_parity == (child_count_if_not_root % 2):
                hol_jjak_match += 1
            else:
                reverse_match += 1
            
            # 이웃 노드 방문
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        # 3. 해당 트리가 홀짝 / 역홀짝 트리가 될 수 있는지 판정
        
        # [역홀짝 조건]을 가진 노드가 딱 1개라면, 그 노드를 루트로 세워 홀짝 트리 제작 가능
        if reverse_match == 1:
            hol_jjak_trees += 1
            
        # [홀짝 조건]을 가진 노드가 딱 1개라면, 그 노드를 루트로 세워 역홀짝 트리 제작 가능
        if hol_jjak_match == 1:
            reverse_hol_jjak_trees += 1

    return [hol_jjak_trees, reverse_hol_jjak_trees]