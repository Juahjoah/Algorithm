T = int(input())


for i in range(T):
    count, inputText = input().split()
    count = int(count)


    answer = ""

    for i in inputText :
        answer += i * count

    print(answer)