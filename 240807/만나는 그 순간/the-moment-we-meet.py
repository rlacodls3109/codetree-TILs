OFFSET = 1000000

N, M = tuple(map(int,input().split()))

# 시간에 대한 배열
A = [0] * (OFFSET+1)
B = [0] * (OFFSET+1)


current_pos_A = 0
current_time_A = 0
current_pos_B = 0
current_time_B = 0

for _ in range(N):
    d, t = tuple(input().split())
    t = int(t)
    if d == 'R':
        for i in range(current_time_A+1,current_time_A+t+1):
            A[i] = current_pos_A + 1
            current_pos_A += 1
        
    elif d == 'L':
        for j in range(current_time_A+1,current_time_A+t+1):
            A[j] = current_pos_A - 1
            current_pos_A -= 1
    current_time_A += t
        
for _ in range(M):
    d, t = tuple(input().split())
    t = int(t)
    if d == 'R':
        for i in range(current_time_B+1,current_time_B+t+1):
            B[i] = current_pos_B + 1
            current_pos_B += 1
        
    elif d == 'L':
        for j in range(current_time_B+1,current_time_B+t+1):
            B[j] = current_pos_B - 1
            current_pos_B -= 1
    current_time_B += t
    max_time = current_time_B
        

for time in range(1,max_time+1):
    if A[time] == B[time]:
        print(time)
        break
    elif time == max_time:
        print(-1)