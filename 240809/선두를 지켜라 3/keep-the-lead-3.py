OFFSET = 1000000

N, M = tuple(map(int,input().split()))

# a,b의 시간에 따른 위치 배열
A = [0] * (OFFSET+1)
B = [0] * (OFFSET+1)

# a의 이동경로 기록
time_a = 1
for _ in range(N):
    v,t = tuple(map(int,input().split()))
    for _ in range(t):
        A[time_a] = A[time_a] + v
        time_a += 1

# b의 이동경로 기록
time_b = 1
for _ in range(M):
    v,t = tuple(map(int,input().split()))
    for _ in range(t):
        B[time_b] = B[time_b] + v
        time_b += 1

# 명예의 전당 배열
# A 선두라면 0, B 선두라면 1, C 선두라면 2
rank = []
for i in range(time_a):
    if A[i] == B[i]:
        rank.append(2)
    
    elif A[i] > B[i]:
        rank.append(0)
    
    elif A[i] < B[i]:
        rank.append(1)

#명예의 전당 배열값이 직전과 달라졌다면 카운트
cnt = 0
for i,now_rank in enumerate(rank):
    if i != 0 and now_rank != rank[i-1]:
        cnt += 1

print(cnt)