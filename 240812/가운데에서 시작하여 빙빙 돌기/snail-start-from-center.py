n = int(input())

#(r,c)가 배열의 범위 내에 있는 지 확인하는 함수
def in_range(r,c):
    return 0 <= r and r < n and 0 <= c and c < n

# L,U,R,D 순
mov_x = [0,-1,0,1]
mov_y = [1,0,-1,0]

# 정답 배열
arr = [
    [0] * n
    for _ in range(n)
]

# 시작 위치, 방향 
x, y = (n-1)//2 , (n-1)//2
n_dir = -1 # 아래 반복문의 시작에서 회전 시 왼쪽이 되도록 -1로 설정

# 1. 값을 채우고
# 2. 시계 반대방향으로 90도 회전했을 때 가정해보기
# 3. if 회전하고 앞으로 갔을 때의 위치가 범위 내에 있고, 값이 채워져 있지 않다면 해당 위치로 이동
# 4. else 이전 방향에서 한칸 앞으로 가기
for i in range(1,n*n+1):
    # 1
    arr[x][y] = i
    # 2
    n_dir_n = (n_dir + 1) % 4
    nx, ny = x + mov_x[n_dir_n], y + mov_y[n_dir_n]

    # 3
    if in_range(nx,ny) and arr[nx][ny] == 0:
        n_dir = n_dir_n
        x,y = nx, ny
    # 4
    else :
        x, y = x+mov_x[n_dir], y + mov_y[n_dir]

# 출력
for ar in arr:
    for elem in ar:
        print(elem,end=" ")
    print()