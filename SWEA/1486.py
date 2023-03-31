# 1486. 장훈이의 높은 선반

# 정해진 높이와의 차이가 최소가 되게 만들기 -> 어쨌든 부분 집합
# (직원의 (index)번호, 합) 
def dfs(n, ssum):
    global ans
    # 최소값 구할 때 항상 성공하는 가지치기
    if ans <= ssum - B :
        return 
    
    # 종료 조건을 설정하기
    if n== N:
        if ssum >= B:                 # 합이 B보다 같거나 커야함.
            ans = min(ans, ssum-B) # 최종 답은 차이였으니까, B를 뺀 값을 저장
        return

    # 재귀 함수 설정해서 돌리기
    dfs(n+1, ssum+lst[n])  # 해당 번호의 직원의 키를 포함하는 경우 -> 합에 그 인덱스 값을 더해주기
    dfs(n+1, ssum)          # 포함하지 않는 경우

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = N * 10000		   # 가능한 최대로 설정
    dfs(0, 0)

    print(f'#{tc} {ans}')