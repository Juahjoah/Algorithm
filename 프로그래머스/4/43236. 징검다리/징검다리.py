
def solution(distance, rocks, n):
    answer = distance    
    
    rocks = sorted(rocks)
    rocks.append(distance)
    
    start = 0
    end = distance
    
    while start <= end:
        mid = (start + end) // 2
        
        delete = 0      # 삭제한 돌의 개수
        prev_rock = 0   # 이전 돌 개수 저장
        
        for rock in rocks:
            if rock - prev_rock <= mid:
                delete += 1
                if delete > n:
                    break
            else:
                prev_rock = rock
        
        if delete > n:
            answer = mid
            end = mid - 1
        else:
            # answer = mid
            start = mid + 1
            

    return answer

# for r in combination(rocks, check_rock_cnt):
#             # 각 거리를 구해서 dis에 저장
#             for rock in r:
                
#         # 조건에 맞으면 dis와 answer 중 작은 값을 answer로 지정
#         answer_list.append(min(dis))