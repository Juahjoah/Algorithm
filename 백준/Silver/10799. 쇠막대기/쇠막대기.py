# 10799. 쇠막대기

import sys
input = sys.stdin.readline

input_list = list(input().rstrip())
stick = 0

answer = 0

for i in range(len(input_list)):
    if input_list[i] == '(':
        stick += 1
    else:
        stick -= 1
        if input_list[i - 1] == '(':
            answer += stick
        else:
            answer += 1

print(answer)