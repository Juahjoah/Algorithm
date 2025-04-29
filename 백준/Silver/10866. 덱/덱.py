# 10866. 덱

'''
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
queue = deque()

for _ in range(N):
    order = input().split()

    if order[0] == 'push_front':
        queue.append(order[1])
    elif order[0] == 'push_back':
        queue.appendleft(order[1])
    elif order[0] == 'pop_front':
        if queue:
            x = queue.pop()
            print(x)
        else:
            print(-1)
    elif order[0] == 'pop_back':
        if queue:
            x = queue.popleft()
            print(x)
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif order[0] == 'back':
        if queue:
            print(queue[0])
        else:
            print(-1)
