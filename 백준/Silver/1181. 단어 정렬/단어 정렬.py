# input 값 받아오기
N = int(input())
inputArr = [input() for _ in range(N)]

# 중복을 제거한 후에 저장
setArr = list(set(inputArr))

# 단어 길이와 단어를 담는 배열을 생성하고 정보 담기 -> 이 배열을 길이순으로 정렬하기
sortArr = []
for i in setArr :
    sortArr.append([len(i), i])

sortArr.sort()

for j in range(len(sortArr)) :
    print(sortArr[j][1])