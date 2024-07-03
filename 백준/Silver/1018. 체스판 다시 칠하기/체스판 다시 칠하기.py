# input 값 받아오기
N, M = map(int, input().split())
# inputArr = [list(input().split()) for _ in range(N)]
inputArr = [input() for _ in range(N)]

# 결과를 담을 빈 배열 -> 원하는 건 최소 변경 횟수 = 결과 중에 최솟값 찾기
result = []

# input 체스판 전체를 돌면서 확인하기
for i in range(N-7):
    for j in range(M-7):

        countW = 0
        countB = 0

        # 8*8로로나눈 그 체스판만 확인하기
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b)%2 == 0:
                    if inputArr[a][b] != "W":
                        countW +=1
                    if inputArr[a][b] != "B":
                        countB += 1

                else:
                    if inputArr[a][b] != "B":
                        countW += 1
                    if inputArr[a][b] != "W":
                        countB += 1

        result.append(countW)
        result.append(countB)

print(min(result))