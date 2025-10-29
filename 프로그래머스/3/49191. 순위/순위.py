def solution(n, results):
    answer = 0
    
    play = [[0] * (n + 1) for _ in range(n + 1)]
    
    # 경기를 진 경우와 이긴 경우를 파악해서 입력
    for a, b in results:
        play[a][b] = 1
        play[b][a] = -1
    
    # 플루이셜-마샬 알고리즘
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if play[i][k] == play[k][j] == 1:
                    play[i][j] = 1
                    play[j][i] = -1
                if play[i][k] == play[k][j] == -1:
                    play[i][j] = -1
                    play[j][i] = 1
                    
    
    for p in play[1:]:
        if p[1:].count(0) == 1:
            answer += 1
    print(play)
                    
    return answer