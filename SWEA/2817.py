# 2817. 부분 수열의 합

# (인덱스 번호, 수열의 합)
def dfs(n, sum):
    global ans
    # 3) 가지치기 : 더 이상 정답 갱신의 가능성이 없을 때,
    # 가장 마지막에, 가장 위쪽에 작성
    if K < sum :
        return

    # 1) 종료조건(n과 관련해서) : 정답처리는 무조건 이 곳에서 진행
    if n == N:
        if sum == K :
            ans += 1
        return

    # 2) 하부호출
    dfs(n+1, sum+lst[n])    # 그 숫자를 선택하는 경우
    dfs(n+1, sum)           # 선택하지 않는 경우

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = 0
    dfs(0, 0)

    print(f'#{tc} {ans}')