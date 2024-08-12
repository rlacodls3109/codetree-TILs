n, m = tuple(map(int,input().split()))

mov_x = [1,0,-1,0]
mov_y = [0,1,0,-1]
n_dir = 0
def in_range(r,c):
    return 0 <= r and r < n and 0 <= c and c < m

arr = [
    [0] * m
    for _ in range(n)
]

x,y = 0,0
for i in range(1,n*m+1):
    arr[x][y] = i
    nx = x + mov_x[n_dir]
    ny = y + mov_y[n_dir]

    if not in_range(nx,ny) or arr[nx][ny] != 0:
        n_dir = (n_dir + 1) % 4
    
    x += mov_x[n_dir]
    y += mov_y[n_dir]


for ar in arr:
    for elem in ar:
        print(elem,end = " ")
    print()