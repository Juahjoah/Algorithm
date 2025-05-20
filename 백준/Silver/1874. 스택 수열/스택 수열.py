# 1874. 스택 수열

import sys
input = sys.stdin.readline

N = int(input())
stack = []
answer = []
cnt = 1

for i in range(N):
    num = int(input())

    while cnt <= num:
        stack.append(cnt)
        answer.append('+')
        cnt += 1

    # while문을 다돌고 stack의 맨위값이 num과 동일하다면 제거
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        break

if stack:
    print("NO")
else:
    for a in answer:
        print(a)