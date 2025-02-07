N, M = map(int, input().split())
tree = list(map(int, input().split()))

left = 0
# right = 10 ** 11
right = max(tree)

H = 0

while left <= right:
    mid = (left + right) // 2

    # 조건을 충족할 수 있게 만드는 코드 구현
    cutting = 0

    for i in range(N):
        if tree[i] > mid:
            cutting += (tree[i] - mid)

    if cutting >= M:
        # left = high
        H = mid
        left = mid + 1
    else:
        right = mid - 1

print(H)