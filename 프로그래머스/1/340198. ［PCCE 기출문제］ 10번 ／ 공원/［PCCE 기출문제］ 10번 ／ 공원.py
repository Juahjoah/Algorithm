def check(mat, park, start_r, start_c):
    for r in range(start_r, start_r + mat):
        for c in range(start_c, start_c + mat):
            if r < len(park) and c < len(park[0]):
                if park[r][c] != "-1":
                    return False
            else:
                return False
    return True

def solution(mats, park):
    answer = 0
    mats.sort(reverse = True)

    rows, cols = len(park), len(park[0])
    
    for mat in mats:
        for r in range(rows):
            for c in range(cols):
                if check(mat, park, r, c):
                    return mat
    return -1