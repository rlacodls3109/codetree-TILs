# 문제의 조건에 따라 배열을 -1000 ~ 1000 범위를 가지도록 2001의 길이로 설정한다.
arr = [0] * 2000 + 1

n = int(input())

#현재 위치 0 -> 인덱스로는 1000
current_point = 1000

for _ in range(n):
    # a = 움직인 거리, b = L,R
    a, b = tuple(input().split())
    a = int(a)

    # R이면 현재 위치에서 더해준다.
    if b == 'R':
        # 구간 단위로 진행하는 문제이므로 맨 뒤 점에 등호가 들어가지 않음   
        # current_point ~ current_point + a 까지 경로 이동
        for i in range(current_point,current_point+a):
            arr[i] += 1 # 배열에 겹치는 구간 체크 
        current_point += a # 현재 위치 갱신
    
    # L이면 현재 위치에서 빼준다.
    elif b == 'L': 
        # current_point - a ~ current 구간의 이동이 이루어짐
        for i in range(current_point - a,current_point):
            arr[i] += 1 # 배열에 겹치는 구간 체크
        current_point -= a # 현재 위치 갱신

# 두 번 이상 지나간 영역의 크기를 구한다.
cnt = 0
for elem in arr:
    if elem >= 2:
        cnt += 1
print(cnt)