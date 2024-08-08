OFFSET = 1000000

n, m = tuple(map(int,input().split()))

# 매 초마다 어느 위치에 있는 지 기록하는 배열
A = [0] * (OFFSET+1)
B = [0] * (OFFSET+1)

#a의 이동경로 기록
a_time = 1
for _ in range(n):
    t,d = tuple(input().split())
    t = int(t)

    for _ in range(t):
        A[a_time] = A[a_time-1] + (1 if d =='R' else -1)
        a_time += 1

#b의 이동경로 기록
b_time = 1
for _ in range(m):
    t,d = tuple(input().split())
    t = int(t)

    for _ in range(t):
        B[b_time] = B[b_time-1] +(1 if d =='R' else -1)
        b_time += 1

# 먼저 이동을 끝낸 사람의 위치배열 값을 이동중인 사람의 시간에 맞추어 마지막지점을 넣어주어야 한다.
if a_time < b_time:
    while(a_time != b_time):
        A[a_time] = A[a_time-1]
        a_time += 1
elif a_time > b_time:
    while(a_time != b_time):
        B[b_time] = B[b_time-1]
        b_time += 1

# 만나는 횟수를 구한다.
cnt = 0
for time in range(1,a_time):
    # 직전에 같은 위치가 아니면서 현재에 같은 위치에 서있을 때 카운트
    if A[time] == B[time] and A[time-1] != B[time-1]:
        cnt += 1

print(cnt)