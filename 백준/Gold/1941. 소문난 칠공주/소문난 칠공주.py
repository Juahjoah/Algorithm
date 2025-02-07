
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def dfs(crews, y_cnt):

    if len(crews) == 7:
        check_crews = tuple(sorted(crews, key = lambda x:(x[0], x[1])))
        if check_crews not in answer_list:
            answer_list.append(check_crews)
            global answer
            answer += 1
        return

    for x, y in crews:
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                visited[nx][ny] = True
                if board[nx][ny] == 'Y':
                    y_cnt += 1

                if y_cnt <= 3:
                    crews.append((nx, ny))
                    dfs(crews, y_cnt)

                # 다시 원상태로 되돌려 주기
                    crews.pop()
                if board[nx][ny] == 'Y':
                    y_cnt -= 1
                visited[nx][ny] = False


board = [list(input()) for _ in range(5)]

visited = [[False] * 5 for _ in range(5)]
answer = 0
answer_list = []

for i in range(5):
    for j in range(5):
        visited[i][j] = True
        if board[i][j] == 'S':
            dfs([(i, j)], 0)
        else:
            dfs([(i, j)], 1)

print(answer)
