from itertools import permutations

# user와 banned가 일치하는지 확인하는 함수
def userMatch(user, banned):
    if len(user) != len(banned):
        return False
    for u, b in zip(user, banned):
        if b == '*':
            continue
        if u != b:
            return False
    return True

def solution(user_id, banned_id):
    possible_matches = []
    
    # 각 banned_id에 대해 매칭될 수 있는 user_id 찾기
    for b in banned_id:
        matches = []
        for u in user_id:
            if userMatch(u, b):
                matches.append(u)
        possible_matches.append(matches)
    
    # 가능한 모든 경우의 수를 찾기 위해 permutations 사용
    allCases = permutations(user_id, len(banned_id))
    
    validCases = set()
    
    for case in allCases:
        match = True
        for i in range(len(banned_id)):
            if not userMatch(case[i], banned_id[i]):
                match = False
                break
        if match:
            validCases.add(frozenset(case))
    
    return len(validCases)

