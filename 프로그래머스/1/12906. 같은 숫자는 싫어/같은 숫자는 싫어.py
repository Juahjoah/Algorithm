def solution(arr):
    stack = []
    number = len(arr)
    stack.append(arr[0])
    
    for i in range(1, number):
        stack.append(arr[i])
        if arr[i] == arr[i-1]:
            stack.pop()
        else:
            continue
    
    return stack