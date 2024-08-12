n, m = tuple(map(int,input().split()))

# 현재 위치가 배열 안에 있는 지 확인하는 함수
def in_range(r,c,n):
    return 0 <= r and r < n and 0 <= c and c < n

# R,D,L,U 순
mov_r = [0,1,0,-1]
mov_c = [1,0,-1,0]
 
# 정답 배열
arr = [
    [0] * n
    for _ in range(n)
]


for _ in range(m):
    r, c = tuple(map(int,input().split()))
    # 실제 위치는 -1
    r, c = r-1, c-1

    #해당 위치를 1로 변경한다
    arr[r][c] += 1
    
    # 해당 위치의 R,D,L,U 에 있는 값을 검사 
    cnt = 0
    for k in range(4):
        nr = r + mov_r[k]
        nc = c + mov_c[k]
        # 배열에서 벗어나지 않고, 1이라면 count
        if in_range(nr,nc,n) and arr[nr][nc] == 1:
            cnt += 1
    
    # count가 3이면 1 출력 아니라면 0 출력
    if cnt == 3:
        print(1)
    else:
        print(0)