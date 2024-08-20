r,c = tuple(map(int,input().split()))

arr = [
    list(input().split())
    for _ in range(r)
]


# 시작 위치와 마지막 위치는 정해져 있음
start_x, start_y = 0,0
end_x , end_y = r-1, c-1

cnt = 0
# (start_x,start_y) -> (i,j) -> (k,l) -> (end_x,end_y)
# 1. 만약 arr[start_x][start_y] 와 arr[i][j]가 다르다면 계속 탐색
    # 이때 i와 j는 시작위치보단 1 이상 커야하고, 마지막 위치에서는 적어도 2만큼 적어야 한다.
# 2. 만약 arr[k][l] 이 arr[i][j]와 다르고, arr[k][l]과 마지막 위치의 값이 다르면 조건에 만족한다.
    # 이때 k,l은 i,j보단 1이상 커야하고, 마지막 위치보단 적어도 1만큼 적어야 한다.
    # 조건에 만족하면 count
for i in range(start_x+1,r-2):
    for j in range(start_y+1,c-2):
        # 1.
        if arr[i][j] != arr[start_x][start_y]:
            for k in range(i+1,r-1):
                for l in range(j+1,c-1):
                    # 2
                    if arr[k][l] != arr[i][j] and arr[k][l] != arr[end_x][end_y]:
                        cnt += 1

print(cnt)