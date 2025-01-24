
def vps(inp):
    stack = []

    for i in inp:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) == 0:
                return "NO"
            stack.pop()

    if stack:
        return "NO"
    return "YES"

N = int(input())
for _ in range(N):
    sentence = list(input())
    print(vps(sentence))

