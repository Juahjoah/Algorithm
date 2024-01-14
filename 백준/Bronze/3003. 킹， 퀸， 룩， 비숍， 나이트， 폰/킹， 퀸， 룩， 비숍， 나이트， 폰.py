T = input()
# T = [0 1 2 2 2 7]

chess_list = [1, 1, 2, 2, 2, 8]
input_list = list(map(int, T.split()))

for i in range(6):
    print(chess_list[i] - input_list[i], end=' ')