def solution(participant, completion):
    runners = {}
    
    for p in participant:
        if p in runners:
            runners[p] += 1
        else:
            runners[p] = 1
            
    for c in completion:
        runners[c] -= 1
        
    for name in runners:
        if runners[name] > 0:
            return name
