OFFSET = 1000000

n, m = tuple(map(int,input().split()))

A = [0] * (OFFSET+1)
B = [0] * (OFFSET+1)

a_time = 1
for _ in range(n):
    t,d = tuple(input().split())
    t = int(t)

    for _ in range(t):
        A[a_time] = A[a_time-1] + (1 if d =='R' else -1)
        a_time += 1


b_time = 1
for _ in range(m):
    t,d = tuple(input().split())
    t = int(t)

    for _ in range(t):
        B[b_time] = B[b_time-1] +(1 if d =='R' else -1)
        b_time += 1

if a_time < b_time:
    while(a_time != b_time):
        A[a_time] = A[a_time-1]
        a_time += 1

elif a_time > b_time:
    while(a_time != b_time):
        B[b_time] = B[b_time-1]
        b_time += 1


cnt = 0

for time in range(1,a_time):
    if A[time] == B[time] and A[time-1] != B[time-1]:
        cnt += 1

print(cnt)