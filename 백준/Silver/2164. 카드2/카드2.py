# 2164. 카드 2

import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
card_list = deque()

for i in range(1, N + 1):
    card_list.append(i)

while len(card_list) > 1:
    card_list.popleft()                        # 제일 위에 있는거 버리기
    card_list.append(card_list.popleft())      # 제일 위에 있는거 뒤로 옮기기

print(*card_list)