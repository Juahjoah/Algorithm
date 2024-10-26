N = int(input())
A = list(map(int, input().split()))
B = set()

for i in A:
    B.add(i)

M = int(input())
input_list = list(map(int, input().split()))


for m in input_list:    
    if m in B:
        print(1)
    else:
        print(0)