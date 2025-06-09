# 2504. 괄호의 값

import sys
input = sys.stdin.readline

input_text = list(input().rstrip())
stack = []
answer = 0
# 값을 잘 계산해 주는 것이 포인트!
cnt = 1

for i in range(len(input_text)):
    char = input_text[i]

    if char == '(':
        cnt *= 2
        stack.append(char)
    elif char == '[':
        cnt *= 3
        stack.append(char)
    elif char == ')' :
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if input_text[i - 1] == '(':
            answer += cnt
        stack.pop()
        cnt //= 2
    else:
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if input_text[i - 1] == '[':
            answer += cnt
        stack.pop()
        cnt //= 3

if stack:
    print(0)
else:
    print(answer)