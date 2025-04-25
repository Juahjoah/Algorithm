from itertools import permutations

while True:
    try:
        text, num = input().split()
        num = int(num)

        cnt = 0
        flag = False

        for p in permutations(text, len(text)):
            cnt += 1
            if cnt == num :
                print(text, num, '=', ''.join(p))
                flag = True
                break

        if not flag:
            print(text, num, '=', 'No permutation')

    except EOFError:
        break

