N = int(input())
input_list = []

for inp in range(N):
    x, y = map(int, input().split())
    input_list.append((x, y))

answer_list = sorted(input_list, key=lambda x:(x[1], x[0]))

for ans in answer_list:
    print(*ans)