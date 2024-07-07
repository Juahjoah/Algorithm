import sys

# inputNum = list(map(int, sys.stdin.read().split()))

# input 받기
N, M, V = map(int, input().split())
dataTree = [[0]*(N+1) for _ in range(N+1)]

# 노드트리를 표현할 행렬 만들기
for i in range(M):
    a, b = map(int, input().split())
    dataTree[a][b] = dataTree[b][a] = 1

# 방문 여부 확인하기
visitedDFS = [0]*(N+1)
visitedBFS = [0]*(N+1)

# DFS 구현
def DFS(V):
    visitedDFS[V] = 1                                    # 방문처리
    print(V, end=' ')                                    # 방문한 노드는 하나씩 출력
    for i in range(1, N+1):
        if dataTree[V][i] == 1 and visitedDFS[i] == 0 :  # 연결되어 있고, 방문하지 않은 노드라면 출력
            DFS(i)


# BFS 구현
def BFS(V):
    queue = [V]                                          # 시작점 담기
    visitedBFS[V] = 1                                    # 방문처리
    while queue :
        V = queue.pop(0)
        print(V, end=' ')
        for j in range(1, N+1):
            if (dataTree[V][j] == 1 and visitedBFS[j] == 0) :
                queue.append(j)
                visitedBFS[j] = 1                        # 방문처리


# 함수 출력
DFS(V)
print()
BFS(V)