N, X = map(int, input().split())
A = list(map(int, input().split()))
answer_list = []

for i in A:
    if i < X:
        answer_list.append(i)
    else:
        continue

# for answer in answer_list:
#     print(answer, end=" ")

print(*answer_list)