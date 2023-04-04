# 5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기

# union-find 구현하기

# 틀이 이미 잡힌 상태, union, find 함수는 그대로 기억했다가 사용해도 괜찮음.
# x를 포함하는 집합이 어떤 것인지 찾는 연산 = 대표원소가 뭔지 찾는 연산
# 재귀적으로 계속 find_set을 하면서 찾아내는 편이 좋음.
def find_set(x):
    if parent[x] == x :
        return x
    else:
        return find_set(parent[x])

# x와 y를 포함하는 두 집합을 통합하는 연산
# (대표 원소가 다른 집합의 대표 원소를 가리키도록 변경)
def union(x, y):
    # 각각의 원소가 각각의 대표 원소
    x = find_set(x)         # x가 속한 집합의 대표 원소
    y = find_set(y)         # y가 속한 집합의 대표 원소

    if rank[x] >= rank[y]:
        parent[y] = x
    else :
        parent[x] = y

    # 같을때만 처리해주기
    if rank[x] == rank[y]:
        rank[x] += 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    # 숫자 두개씩 한세트! -> 일단 리스트로 전체를 받아보기
    parent = [i for i in range(N+1)]
    rank = [0] * (N+1)

    # 만들어진 값을 union으로 하나로 뭉치고
    for i in range(M):
        union(data[2*i], data[2*i+1])

    groups = set()         # w 중복 제거용
    for j in range(1, N+1):
        groups.add(find_set(j))

    # 어쨌든 만들어진 조건에 맞는 답을 출력하려면, len으로 숫자를 세면됨.
    print(f'#{tc} {len(groups)}')