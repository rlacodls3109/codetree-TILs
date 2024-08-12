n, m = tuple(map(int,input().split()))

# D, R, U, L 순서
mov_x = [1,0,-1,0]
mov_y = [0,1,0,-1]
n_dir = 0

def in_range(r,c):
    return 0 <= r and r < n and 0 <= c and c < m

# 정답 배열 생성
arr = [
    [0] * m
    for _ in range(n)
]

# 맨 처음 위치
x,y = 0,0
for i in range(1,n*m+1):
    # 현 위치에 값을 채움
    arr[x][y] = i 
    # 현재 방향을 기준으로 그 다음 위치 값 계산
    nx = x + mov_x[n_dir]
    ny = y + mov_y[n_dir]

    # 다음 위치가 배열의 범위를 벗어나거나, 값이 채워져 있을 경우,
    # 방향을 시계반대방향으로 전환
    if not in_range(nx,ny) or arr[nx][ny] != 0:
        n_dir = (n_dir + 1) % 4
    
    # x,y값 갱신
    x += mov_x[n_dir]
    y += mov_y[n_dir]


for ar in arr:
    for elem in ar:
        print(elem,end = " ")
    print()