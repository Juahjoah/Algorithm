# 2877. 4와 7

def check_num(a, b, K):
    answer = ''
    while K > 0:
        l = K % 2           # 짝수, 홀수 판단
        K = K // 2
        if l == 0:          # 짝수인 경우,
            K -= 1
            answer = b + answer
        else:               # 홀수인 경우,
            answer = a + answer

    print(answer)

K = int(input())
check_num('4', '7', K)



