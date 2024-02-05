# 첫 번째 줄: 상근이가 가지고 있는 숫자 카드의 개수 N
N = int(input())
# 두 번째 줄: 숫자 카드에 적혀있는 정수들
cards = list(map(int, input().split()))

# 세 번째 줄: 구해야 할 숫자 카드의 개수 M
M = int(input())
# 네 번째 줄: 구해야 할 숫자 카드들
query_numbers = list(map(int, input().split()))

# 각 숫자 카드가 몇 개 있는지 저장할 딕셔너리
card_counts = {}

# 상근이가 가지고 있는 카드의 등장 횟수를 계산
for card in cards:
    if card in card_counts:
        card_counts[card] += 1
    else:
        card_counts[card] = 1

# 결과를 저장할 리스트
answer = []

# 구해야 할 숫자 카드들에 대해 각각 몇 개 있는지 확인
for query in query_numbers:
    answer.append(card_counts.get(query, 0))

# 결과 출력
print(' '.join(map(str, answer)))
