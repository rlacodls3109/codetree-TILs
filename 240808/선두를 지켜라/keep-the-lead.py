OFFSET = 1000
n, m = tuple(map(int,input().split()))

# 매 시간마다의 거리를 저장하는 배열
A = [0] * (OFFSET+1)
B = [0] * (OFFSET+1)

# a의 이동거리를 기록
a_time = 0
for _ in range(n):
    v, t = tuple(map(int,input().split()))

    for _ in range(t):
        A[a_time + 1] = A[a_time] + v
        a_time += 1

# b의 이동거리를 기록
b_time = 0
for _ in range(m):
    v, t = tuple(map(int,input().split()))

    for _ in range(t):
        B[b_time + 1] = B[b_time] + v
        b_time += 1

#선두로 가는 사람 추가할 배열
winner = []

# 1초부터 이동한 시간까지 매 시간마다 A,B의 위치를 비교하였을 때 
#A 면 0, B이면 1
for i in range(1,a_time):
    winner.append(0 if A[i] >= B[i] else 1)

ans = 0

for i,elem in enumerate(winner):
    #선두가 바뀔 때의 횟수를 센다
    if i != 0 and elem != winner[i-1]:
        ans += 1

print(ans)