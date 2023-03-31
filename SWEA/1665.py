# 1865. 동철이의 일 분배

# sys.float_info.epsilon : 부동소수점에서 해당 언어가 어느 정도 범위 안에서 오차를 받게되는가?

# 백트래킹 함수 만들기
# (인덱스, 현재 확률_성공할 수 있는가 아닌가)
def backtrack(idx, cur):
    global res
    # 백트래킹 :
    if cur <= res :
        return

    # 종료조건
    if idx == N :
        res = max(cur, res)

    # 하부함수
    for i in range(N):
        if not visited[i]:
            visited[i] = 1                          # 방문 표시
            backtrack(idx+1, cur * arr[idx][i])     # cur 계속해서 갱신
            visited[i] = 0                          # 초기화

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # arr = [list(map(int, input().split())) for _ in range(N)]
    # # 입력을 받고, 입력받은 값을 100으로 나눠 실수형으로 만들기
    # for i in range(N):
    #     for j in range(N):
    #         arr[i][j] = arr[i][j] / 100
    # 아예 받을 때부터 바꿔보자! -> int로 받고 100으로 나누기
    arr = [list(map(lambda p:int(p)/100, input().split())) for _ in range(N)]

    visited = [0] * N           # 어떤 특정 값을 할당했는지 아닌지 확인할 리스트
    res = 0                     # 최종결과 변수
    backtrack(0, 1)             # 확률이 1 = 100%

    print(f'#{tc}{res*100 : 6f}')

# 소수점 6자리까지만 출력
#1 0.4965456
#2 0.23362170493453494
#3 0.32
#4 0.338044889479752
#5 0.166959050729942
#6 0.14878079999999996
#7 0.045593598077808085
#8 0.07764233056568766
#9 0.26789665667154416
#10 0.7656