n, t = tuple(map(int,input().split()))
order = input()

# 현재 위치가 범위 내에 있는 지 확인
def in_range(r,c):
    return 0 <= r and r < n and 0 <= c and c < n

# N,E,S,W 순
mov_x = [-1,0,1,0]
mov_y = [0,1,0,-1]

# 초기값 및 초기 방향
x,y = (n-1)//2, (n-1)//2
n_dir = 0

# 격자 정보
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

# 시작 위치를 총 합에 포함
sum_arr = arr[x][y]

for i in range(t):
    # 시계방향으로 90도 회전
    if order[i] == 'R':
        n_dir = (n_dir+1) % 4
    
    # 시계 반대방향으로 90도 회전
    elif order[i] == 'L':
        n_dir = (n_dir+3) % 4
    
    # 앞으로 가기
    elif order[i] == 'F':
        # 앞으로 갔을 때 위치가 배열의 범위 내에 있다면 이동 후 합
        nx,ny = x+mov_x[n_dir], y+mov_y[n_dir]
        if in_range(nx,ny):
            x, y = nx, ny
            sum_arr += arr[x][y]
        else : # 아니라면 명령을 무시한다.
            continue

print(sum_arr)