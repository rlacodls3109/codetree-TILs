# k가 주어졌을 때, 0~25까지 A~Z로 바꾸는 함수
# 26이면 다시 0으로 변경해야 하므로 나머지 연산
def alpha(k):
    num = (k % 26) + 65
    return chr(num)


n,m = tuple(map(int,input().split()))

# 해당 위치가 배열의 범위 내에 있는 지 확인하는 함수
def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

# R,D,L,U 순임
mov_x = [0,1,0,-1]
mov_y = [1,0,-1,0]

# 정답 배열
arr = [
    [0]*m
    for _ in range(n)
]

#초기 위치, 방향
x, y = 0,0
n_dir = 0

#첫번째 배열의 값을 넣는다.
arr[x][y] = alpha(0)

for i in range(1, n*m):
    # 현재 방향에서 진행할 수 있는 위치로 회전할 때 까지 무한루프
    while(1):
        nx, ny = x + mov_x[n_dir] , y+mov_y[n_dir]
        if in_range(nx,ny) and arr[nx][ny] == 0:
            break
        
        else: # if 문 만족하지 않으면 방향 시계방향 90도로 전환
            n_dir = (n_dir + 1) % 4
    
    # 바뀐 위치로 이동 후 값 채우기
    x, y = nx, ny
    arr[x][y] = alpha(i)


# 출력
for ar in arr:
    for elem in ar:
        print(elem, end = " ")
    print()