import sys

# 전체 입력을 받아와서 각 줄을 분리하여 리스트로 저장
inputNum = list(map(int, sys.stdin.read().split()))

# 리스트에서 가장 큰 값과 그 값의 인덱스 찾기
maxNum = max(inputNum)
# 인덱스는 0부터 시작하기 때문에 실제 인덱스에 1을 더해줌
maxIndex = inputNum.index(maxNum) + 1 

# 가장 큰 값과 그 값의 인덱스를 출력
print(maxNum)
print(maxIndex)
