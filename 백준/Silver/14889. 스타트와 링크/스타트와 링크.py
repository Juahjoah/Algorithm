from itertools import combinations

def check_player(play, m):
    player_cases = list(combinations(play, m))
    team_number = len(player_cases)//2
    global answer

    for c in range(team_number):
        # 팀 나누기
        start = player_cases[c]
        link = player_cases[-1 - c]

        start_team = 0
        link_team = 0

        # 각 팀의 능력 측정
        for i in range(0, m-1):
            for j in range(i+1, m):
                start_team += board[start[i]][start[j]]
                start_team += board[start[j]][start[i]]
                link_team += board[link[i]][link[j]]
                link_team += board[link[j]][link[i]]

        # 최솟값 비교해서 answer 갱신
        answer = min(answer, abs(start_team - link_team))

    return answer


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

answer = 100
player_list = []
m = n//2

for player in range(n):
    player_list.append(player)

print(check_player(player_list, m))
