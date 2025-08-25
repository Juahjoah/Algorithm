# 괄호

import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    input_text = list(input().strip())
    stack = []

    for i in range(len(input_text)):
        if input_text[i] == '(':
            stack.append(input_text[i])
        else:
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(')')
                    break
            else:
                stack.append(')')
                break

    if stack:
        print("NO")
    else:
        print("YES")