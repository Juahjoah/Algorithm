from collections import deque

def BFS(begin, target, words):
    queue = deque([(begin, 0)])
    visited = set()

    while queue:
        current_word, steps = queue.popleft()
        if current_word == target:
            return steps

        for word in words:
            if word not in visited and isOneLetter(current_word, word):
                visited.add(word)
                queue.append((word, steps + 1))

    return 0

def isOneLetter(word1, word2):
    diff_count = sum(1 for a, b in zip(word1, word2) if a != b)
    return diff_count == 1


def solution(begin, target, words):
    # target이 words에 없으면 변환할 수 없음
    if target not in words:
        return 0

    return BFS(begin, target, words)

    
