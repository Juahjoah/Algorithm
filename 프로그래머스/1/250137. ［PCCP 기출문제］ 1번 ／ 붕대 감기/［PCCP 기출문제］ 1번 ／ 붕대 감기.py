def solution(bandage, health, attacks):
    t, x, y = bandage
    max_health = health
    
    time = 0
    attack = 0
    hp_time = 0
    
    while time <= attacks[-1][0]:    
        next_attack = attacks[attack][0]
        
        if time == next_attack: # 공격 성공
            health -= attacks[attack][1]
            attack += 1
            hp_time = 0
            
            if health <= 0:
                health = -1
                break 
        else:   # 체력 회복
            if health < max_health:
                health = min(max_health, health + x)
            
            hp_time += 1
            
            if hp_time == t:
                if health < max_health:
                    health = min(max_health, health + y)
                hp_time = 0

        time += 1

    return health