

def BFS(i):
    # visited = [[0]*(computer+1) for _ in range(computer+1)]
    visited = [0]*(computer+1)
    visited[1] = 1
    answer = 0
    queue = []
    queue.append(i)

    while queue:
        num = queue.pop(0)
        
        for j in range(1, computer+1):
            if board[num][j] == 1 and visited[j] == 0:
                visited[j] = 1
                queue.append(j)
                answer += 1

    return answer

computer = int(input())
link = int(input())
input_list = [list(map(int, input().split())) for _ in range(link)]

board = [[0]*(computer+1) for _ in range(computer+1)]
for inp in input_list:
    board[inp[0]][inp[1]] = 1
    board[inp[1]][inp[0]] = 1

print(BFS(1))