N = int(input())
meetings = []

for i in range(N):
    start, end = map(int, input().split(" "))
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0]))

time = 0
cnt = 0
for meeting in meetings:
    if time <= meeting[0]:
        time = meeting[1]
        cnt += 1

print(cnt)