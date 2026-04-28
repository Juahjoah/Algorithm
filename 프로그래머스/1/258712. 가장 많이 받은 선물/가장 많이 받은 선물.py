def solution(friends, gifts):
    n = len(friends)
    
    # 인덱스 값을 확인하기 위해 친구 이름과 인덱스를 매핑
    index = {}
    for idx, name in enumerate(friends):
        index[name] = idx
    
    # 각 인원 당 선물을 주고 받은 상황을 가정해 그래프 생성
    graph = [[0]*n for _ in range(n)]
    
    for gift in gifts:
        a, b = gift.split()
        graph[index[a]][index[b]] += 1

    # 각 친구의 선물 지수
    score = [0] * n
    
    for i in range(n):
        give = sum(graph[i])
        receive = sum(graph[j][i] for j in range(n))
        score[i] = give - receive    
        
    result = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            # a와 b가 선물을 주고 받은 횟수를 확인
            if graph[i][j] > graph[j][i]:
                result[i] += 1
            elif graph[i][j] < graph[j][i]:
                result[j] += 1
            # 횟수가 같은 경우, score로 비교
            else:
                if score[i] > score[j]:
                    result[i] += 1
                elif score[i] < score[j]:
                    result[j] += 1
    
    return max(result)