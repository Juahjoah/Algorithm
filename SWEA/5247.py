# 5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산

# queue로 돌리면, 시간초과가 발생함. => dequeue를 이용하자!
# 재귀는 깊이제한, 시간제한에 걸릴 확률이 존재함. => BFS로 가능한 연산을 queue에 담아 진행

# 조건 : 4종류 연산, 범위 내(1~10^6), 중복X
from collections import deque

def bfs(start, end):
    q = deque()             # deque로 queue를 만들어 시간초과를 예방
    visited = [0] * 1000001 # 10^6 범위

    q.append(start)         # 시작점을 q에 담아서 진행
    visited[start] = 1      # visited 배열에 1로 표시 -> 초기값이 1이었으니까, 정답부분에서는 꼭 -1 해서 반환

    while q :               # q가 빌때까지 탐색을 반복하기
        c = q.popleft()     # bfs에서 queue.pop(0)하는 것과 동일한 수행,
        # 여기서 시간복잡도를 살펴보면, pop은 O(n), popleft는 O(1)이 되기 때문에 시간 차이가 존재할 수밖에 없음.
        if c == end :       # q에서 꺼낸 답이 최종정답일때, 정답을 찾으면 stop
            return visited[c]-1     # 이미 시작할때 queue에 담으면서+1 로 시작했으니까,

        # 4종류, 범위 내, 중복X
        for n in ((c+1), (c-1), (c*2), (c-10)):       # 원하는 범위 순환
            if 1 <= n <= 1000000 and visited[n] == 0: # 범위 내에 존재하고, 연산을 통해 만들어진적 없다면,
                q.append(n)                           # q에 담고,
                visited[n] = visited[c] + 1           # visited에 해당 숫자를 만드는데 걸린 연산 횟수를 저장

    # queue가 끝났지만, 못찾아 갔다면? -> 만들 수 없는 숫자(이 경우는 발생X)
    return -1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N : 시작 숫자, M : 최종 원하는 숫자

    ans = bfs(N, M)

    print(f'#{tc} {ans}')


'''
queue deque([2])
visited [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
queue deque([3, 1, 4])
visited [0, 2, 1, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
queue deque([1, 4, 6])
visited [0, 2, 1, 2, 2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
queue deque([4, 6])
visited [0, 2, 1, 2, 2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
queue deque([6, 5, 8])
visited [0, 2, 1, 2, 2, 3, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
queue deque([5, 8, 7])
visited [0, 2, 1, 2, 2, 3, 3, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
queue deque([8, 7, 10])
visited [0, 2, 1, 2, 2, 3, 3, 4, 3, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0]
queue deque([7, 10, 9])
visited [0, 2, 1, 2, 2, 3, 3, 4, 3, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''