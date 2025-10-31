
def DFS(numbers, target, current, idx):
    cnt = 0
    if idx == len(numbers):
        if current == target:
            cnt += 1
        return cnt
    
    cnt += DFS(numbers, target, current + numbers[idx], idx + 1)
    cnt += DFS(numbers, target, current - numbers[idx], idx + 1)
    
    return cnt

def solution(numbers, target):
    answer = 0
    answer = DFS(numbers, target, 0, 0)
    
    return answer