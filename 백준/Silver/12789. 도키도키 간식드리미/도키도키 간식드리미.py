def check_number():
    stack = []
    current = 1  # 지금 순서를 저장할 변수
    index = 0    # 대기열을 확인할 인덱스 값

    # 번호 순서대로 통과하는 로직 구현
    while index < N or (stack and stack[-1] == current):
        # 대기열 맨 앞의 학생 번호가 순서와 일치하는 경우
        if index < N and input_list[index] == current:
            current += 1
            index += 1

        # 대기열의 맨 앞의 번호가 일치하지 않으면 스택에 추가하고 다음 숫자로 넘어가기
        elif index < N and input_list[index] != current:
            stack.append(input_list[index])
            index += 1

        # 스택의 맨 위의 값이 현재 간식 번호와 일치하는 경우
        while stack and stack[-1] == current:
            stack.pop()
            current += 1


    if len(stack) == 0 and current == N+1: # 스택이 비어있고, 간식의 순서가 동일하다면,
        print("Nice")
    else:
        print("Sad")



N = int(input())
input_list = list(map(int, input().split()))

check_number()
