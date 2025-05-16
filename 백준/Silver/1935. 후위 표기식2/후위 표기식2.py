# 1935. 후위 표기식

import sys
input = sys.stdin.readline

N = int(input())
input_equation = list(input().rstrip())
input_number = list(int(input()) for _ in range(N))

stack = []

for i in input_equation:
    if 'A' <= i <= 'Z':                           # 알파벳인 경우에 값 변환해서 stack에 담기
        stack.append(input_number[ord(i) - 65])

    else:
        a = stack.pop()
        result = stack.pop()

        if i == '+':
            result += a
        elif i == '-':
            result -= a
        elif i == '*':
            result *= a
        elif i == '/':
            result /= a

        stack.append(result)


print('%.2f' %stack[0])
