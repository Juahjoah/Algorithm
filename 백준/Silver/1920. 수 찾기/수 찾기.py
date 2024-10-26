

def binary_search(left, right):

    while left <= right:
        mid = (left+right) // 2

        if m > A[mid]:
            left = mid + 1
        elif m < A[mid]:
            right = mid - 1
        else:
            left = mid
            right = mid
            break

    if left == mid and right == mid:
        print(1)
    else:
        print(0)





N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
input_list = list(map(int, input().split()))


for m in input_list:
    left = 0
    right = N - 1

    binary_search(left, right)
