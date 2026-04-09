def move(r1, c1, r2, c2):
    path = [(r1, c1)]
    # 먼저 r부터 이동
    while r1 != r2:
        if r1 < r2:
            r1 += 1
            path.append((r1, c1))
        else:
            r1 -= 1
            path.append((r1, c1))
    # c 이동
    while c1 != c2:
        if c1 < c2:
            c1 += 1
            path.append((r1, c1))
        else:
            c1 -= 1
            path.append((r1, c1))
    
    return path

def solution(points, routes):
    answer = 0
    node_routes = []
    for route in routes:
        # 각 상황마다 이동하는 값을 리스트에 저장
        full_path = []
        for i in range(len(route) - 1):
            start = route[i]
            end = route[i + 1]
        
            r1, c1 = points[start - 1]
            r2, c2 = points[end - 1]
        
            path = move(r1, c1, r2, c2)
            if i == 0:
                full_path += path
            else:
                full_path += path[1:]
        
        node_routes.append(full_path)
    
    max_time = max(len(path) for path in node_routes)
    for t in range(max_time):
        pos_count = {}
        for path in node_routes:
            if t < len(path):
                pos = path[t]
                
                if pos in pos_count:
                    pos_count[pos] += 1
                else:
                    pos_count[pos] = 1
    
        for c in pos_count.values():
            if c >= 2:
                answer += 1
    
    return answer