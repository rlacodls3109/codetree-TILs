n = int(input())

def in_range(r,c):
    return 0 <= r and r < n and 0 <= c and c < n

mirrors = []

for i in range(n):
    mirror = input()
    
    mirrors.append([])
    for j,m in enumerate(mirror):
        mirrors[i].append(m) 

#현재 레이저의 방향 D,L,U,R 방향 순으로
mov_r = [1,0,-1,0]
mov_c = [0,-1,0,1]

K = int(input())
K -= 1
n_dir = K // n

if n_dir == 0 :
    x = 0
    y = K % n
elif n_dir == 1:
    x = K % n
    y = n - 1
elif n_dir == 2:
    x = n - 1
    y = n - (K % n) -1
elif n_dir == 3:
    x = n - (K % n) -1
    y = 0

cnt = 0
#배열의 범위 밖이라면 종료
while(in_range(x,y)): 
    cnt += 1 
    if mirrors[x][y] == '\\':
        n_dir = 3 - n_dir

    elif mirrors[x][y] == '/':
        if n_dir == 2 or n_dir == 3:
            n_dir = 5 - n_dir
        elif n_dir == 0 or n_dir == 1:
            n_dir = 1 - n_dir
        
    x += mov_r[n_dir]
    y += mov_c[n_dir]

print(cnt)