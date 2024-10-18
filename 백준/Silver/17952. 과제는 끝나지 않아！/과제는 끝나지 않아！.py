
N = int(input())
answer = 0        # 누적 점수를 담을 변수
stack = []

for i in range(N):
    input_list = list(map(int, input().split()))

    if len(input_list) > 1:
        stack.append(input_list)

    if stack: # 스택에 값이 있다면,
        # 맨 앞에 있는 stack의 time 값을 계속 빼준다!
        stack[-1][2] -= 1
        if stack[-1][2] == 0: # 업무가 끝났다면,
            answer += stack.pop()[1]

print(answer)