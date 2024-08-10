n, m = tuple(map(int,input().split()))

# R:0, D:1, L:2, U:3
dx, dy = [0,1,0,-1], [1,0,-1,0]

#초기값 x, y, 방향을 설정
x,y = 0,0
now_d = 0

# n*m 크기의 배열 설정
answer = [
    [0] * m
    for _ in range(n)
]

# 배열의 범위 안에 있는 위치인 지 확인하는 함수
def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

# (0,0) 은 1
answer[x][y] = 1

# 마지막 번호는 n*m
for i in range(2,n*m+1):
    # 현재 방향을 기준으로 그 다음의 위치값 계산
    nx, ny = x+dx[now_d], y+dy[now_d]

    # 더이상 나아갈 수 없다면 시계방향으로 90도 회전
    if not in_range(nx,ny) or answer[nx][ny] != 0:
        now_d = (now_d + 1)
    
    # 그 다음 위치로 이동
    x,y = x+dx[now_d], y+dy[now_d]
    # 값 채워넣기
    answer[x][y] = i

#출력
for arr in answer:
    for elem in arr:
        print(elem,end=" ")
    print()