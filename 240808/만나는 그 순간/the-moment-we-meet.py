OFFSET = 1000000

N, M = tuple(map(int,input().split()))

# 시간에 대한 위치 배열
A = [0] * (OFFSET+1)
B = [0] * (OFFSET+1)


# A가 매 초마다 서있는 위치를 기록
time_A = 0
for _ in range(N):
    d, t = tuple(input().split())
    t = int(t)
    for _ in range(t):
        time_A += 1
        # 전 시간의 위치에 대해 +1(오른 이동) 혹은 -1(왼쪽 이동)
        A[time_A] = A[time_A - 1] + (1 if d =='R' else -1)
     

# B가 매 초마다 서있는 위치를 기록
time_B = 0
for _ in range(M):
    d, t = tuple(input().split())
    t = int(t)
    for _ in range(t):
        time_B += 1
        B[time_B] = B[time_B - 1] + (1 if d =='R' else -1)

'''
# 조금 더 간결하게 만들 수 있삼..
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
'''

ans = -1
# 이동한 시간인 time_A와 time_B는 동일하므로 범위를 1~time_A로 설정
for time in range(1,time_A):
    if A[time] == B[time]: #같은 시간에 같은 위치가 되는 첫번째 지점의 시간 구하기
        ans = time
        break

print(ans)