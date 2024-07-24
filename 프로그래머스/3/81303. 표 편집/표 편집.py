def solution(n, k, cmd):

    answer = ['O'] * n
    # 스택을 사용하여 삭제된 행을 저장
    removedStack = []
    # 현재 행
    curr = k
    # 이전, 다음 인덱스
    prev = [i - 1 for i in range(n)]
    next = [i + 1 for i in range(n)]
    # 마지막 행 이후의 값은 존재하지 않음
    next[-1] = -1

    for command in cmd:
        # 삭제
        if command[0] == "C":
            # 현재 행 삭제
            removedStack.append((curr, prev[curr], next[curr]))
            answer[curr] = 'X'

            # 연결 끊기
            if prev[curr] != -1:
                next[prev[curr]] = next[curr]
            if next[curr] != -1:
                prev[next[curr]] = prev[curr]

            # 현재 행 업데이트
            if next[curr] != -1:
                curr = next[curr]
            else:
                curr = prev[curr]

        # 복구
        elif command[0] == "Z":
            r, p, n = removedStack.pop()
            answer[r] = 'O'

            if p != -1:
                next[p] = r
            if n != -1:
                prev[n] = r

        # 선택
        elif command[0] == "U":
            X = int(command.split()[1])
            for _ in range(X):
                curr = prev[curr]

        elif command[0] == "D":
            X = int(command.split()[1])
            for _ in range(X):
                curr = next[curr]

    return ''.join(answer)