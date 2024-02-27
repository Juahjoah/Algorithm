import sys
import math

# input = sys.stdin.readline 

N = int(input())
inputArr = [list(map(int, input().split())) for _ in range(N)]

# 거리 계산 함수
def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# 모든 체크포인트를 순서대로 방문했을 때의 총 거리 계산
total_distance = sum(distance(inputArr[i], inputArr[i+1]) for i in range(N-1))

# 각 체크포인트를 건너뛰었을 때 절약할 수 있는 거리 계산
max_saved = 0
for i in range(1, N-1):  # 첫 번째와 마지막 체크포인트는 제외
    # 현재 로직 수정: i를 건너뛰고 i-1에서 i+1로 직접 갔을 때 절약되는 거리
    skip_distance = distance(inputArr[i-1], inputArr[i+1])
    current_distance = distance(inputArr[i-1], inputArr[i]) + distance(inputArr[i], inputArr[i+1])
    saved = current_distance - skip_distance
    max_saved = max(max_saved, saved)

# 최소 거리 계산
answer = total_distance - max_saved

print(answer)
