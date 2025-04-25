from itertools import combinations

while True:
    input_num = input().split()
    if input_num[0] == '0':
        break

    K = int(input_num[0])
    S = input_num[1:]

    for i in combinations(S, 6):
        print(' '.join(i))
    print()
