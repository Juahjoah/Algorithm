# 2531. 회전초밥

N, d, k, c = map(int, input().split())
input_list = [int(input()) for _ in range(N)]
input_list += input_list[:k - 1]                # 연결되어 있으니까 부족한 k만큼 추가

# 가장 큰 숫자는 9천만. → for 문 2개 돌리면 1억 8천개의 연산이 진행됨.
# → for문을 돌면서 매번 배열을 생성하는 게 아니라 슬라이싱 윈도우를 활용

# 연속된 k개의 초밥의 종류 파악하기
sushi_type = [0] * (d + 1)                  # 스시의 종류별 개수를 담을 리스트
answer = 0

# 쿠폰(c) 초밥 확인
sushi_type[c] += 1
sushi_cnt = 1

for i in range(k):
    if sushi_type[input_list[i]] == 0:      # 처음 등장한 초밥이라면,
        sushi_cnt += 1                      # 초밥 종류 수 추가
    sushi_type[input_list[i]] += 1          # 초밥 갯수 증가

answer = sushi_cnt

# 슬라이딩 윈도우 : 시작 값 빼고 다음 값 추가하기
for j in range(N - 1): # N까지 하면 어차피 처음 값과 같아져서 굳이 할 필요 없음.
    sushi_type[input_list[j]] -= 1
    if sushi_type[input_list[j]] == 0:
        sushi_cnt -= 1
    sushi_type[input_list[k + j]] += 1
    if sushi_type[input_list[k + j]] == 1:
        sushi_cnt += 1

    answer = max(answer, sushi_cnt)

print(answer)