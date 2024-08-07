OFFSET = 1000
N, M = tuple(map(int,input().split()))

A = [0] * (2*OFFSET+1)
B = [0] * (2*OFFSET+1)

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
        

for time in range(1,2*OFFSET+1):
    if A[time] == B[time]:
        print(time)
        break