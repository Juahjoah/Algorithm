

def calculation(A, B, C):
    for i in range(B):
        if B == 1 :
            return A % C

        val = calculation(A, B//2, C)
        # 짝수인 경우,
        if B % 2 == 0:
            return (val * val) % C
        # 홀수인 경우,
        else:
            return (val * val * A) % C




A, B, C = map(int, input().split())

print(calculation(A, B, C))