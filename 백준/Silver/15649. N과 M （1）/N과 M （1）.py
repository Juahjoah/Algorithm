n, m = list(map(int, input().split()))
# inputArr = [i for i in range(1, n+1)]
inputArr = []

def Backtracking():
    if len(inputArr) == m:
        print(' '.join(map(str,inputArr)))
        return

    for i in range(1, n+1):
        if i not in inputArr:
            inputArr.append(i)
            Backtracking()
            inputArr.pop()

Backtracking()
