OFFSET = 100 # -100~100으로 좌표평면 범위를 지정하므로 offset 상수 선언
LEN = 8 #색종이의 길이가 8로 정해져 있으므로 상수로 선언

# 좌표평면을 나타내는 2차원 배열 
rec = [
    [0] * (2*OFFSET + 1)
    for _ in range(2*OFFSET + 1)
]

N = int(input())


for _ in range(N):
    #좌측 하단의 좌표를 입력받음
    x, y = tuple(map(int,input().split()))

    # (x,y) 부터 (x+8,y+8) 범위의 사각형을 칠한다.
    for i in range(x+OFFSET,x+LEN+OFFSET):
        for j in range(y+OFFSET,y+LEN+OFFSET):
            if rec[i][j] <= 0:
                rec[i][j] = 1

# 넓이 구하기
area = 0
for arr in rec:
    for elem in arr:
        if elem == 1:
            area += 1

print(area)