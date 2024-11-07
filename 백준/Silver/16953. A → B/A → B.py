from collections import deque

A, B = map(int, input().split())

def multiply(num):
    num = num * 2
    return num

def plus(number):
    number = number * 10 + 1
    return number

def BFS(n):
    queue = deque()
    queue.append((n, 0))

    visited = set()

    while queue:
        x, cnt = queue.popleft()

        if x == B:
            return cnt + 1

        # 아직 B에 도달하지 못한 경우 계속해서 숫자를 변경해줘야함.
        if 1 <= multiply(x) <= 10 ** 9 and multiply(x) not in visited:
            queue.append((multiply(x), cnt+1))
            visited.add(multiply(x))
        if 1 <= plus(x) <= 10 ** 9 and plus(x) not in visited:
            queue.append((plus(x), cnt+1))
            visited.add(plus(x))

    return -1

print(BFS(A))