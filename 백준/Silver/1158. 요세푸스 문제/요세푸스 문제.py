from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque()
answer_list = []

for i in range (1, N + 1):
    queue.append(i)

while queue:
    # if len(queue) >= K:
    #     x = queue[K]
    #     answer_list.append(x)
    #     queue.remove(queue[K])

    for _ in range(K - 1):
        queue.append(queue.popleft()) # K번째 앞에 있는 값들 꺼내서 뒤로 붙이기
    answer_list.append(queue.popleft()) # K번째 값 뽑아서 넣기

print('<' + ', '.join(map(str, answer_list)) + '>')