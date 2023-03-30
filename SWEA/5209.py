# 파이썬 SW문제해결 응용_구현 - 05 백트래킹
# [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용

def dfs(n, sum):
    global ans

    # 가지치기: 더 이상 정답갱신 가능성이 없는 경우 차단
    # 이 부분 생략하면 시간초과 위험 존재
    if ans <= sum:  # 전형적인 최소값문제의 가지치기
        return

    # 종료조건 (n관련)
    if n == N:
        ans = min(ans, sum)
        return

    # 하부호출(중복체크후 가능한 경우 호출)
    for j in range(N):
        if v[j] == 0:           # 미방문
            v[j] = 1            # 방문표시
            dfs(n + 1, sum + arr[n][j])
            v[j] = 0            # 재귀함수이기 때문에 반드시 다시 초기화!


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    v = [0] * N
    ans = N * 99                 # 최소값: 처리중 무조건 갱신되도록 최악의 값(최대값)으로 초기화

    dfs(0, 0)
    print(f'#{test_case} {ans}')
