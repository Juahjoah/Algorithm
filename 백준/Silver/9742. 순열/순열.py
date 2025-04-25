from itertools import permutations

while True:
    try:
        text, num = input().split()
        num = int(num)

        cnt = 0
        flag = False

        for i in permutations(text, len(text)):
            cnt += 1
            if cnt == num:
                print(text, num, '=', ''.join(i))
                flag = True
                break
            if cnt > num - 1:
                print('No permutation')

        if not flag:
            print(text, num, '=', 'No permutation')

    except EOFError:
        break

