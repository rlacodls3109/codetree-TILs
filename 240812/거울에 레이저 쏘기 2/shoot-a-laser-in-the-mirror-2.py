n = int(input())

#현 위치가 배열의 범위를 벗어나지 않는 지 확인하는 함수
def in_range(r,c):
    return 0 <= r and r < n and 0 <= c and c < n

mirrors = []

#
for i in range(n):
    mirror = input()
    
    mirrors.append([])
    for m in mirror:
        mirrors[i].append(m) 

#현재 레이저의 방향 D,L,U,R 방향 순으로
mov_r = [1,0,-1,0]
mov_c = [0,-1,0,1]

# 레이저를 쏘는 위치
K = int(input())

# 주어진 숫자를 n으로 나눈 몫과 나머지를 통해 최초 방향과 위치를 정할 수 있다.
# 몫 : 레이저를 쏘는 방향
k = K - 1
n_dir = k // n

if n_dir == 0 : #(0,k%n)
    x = 0
    y = k % n
elif n_dir == 1: #(k%n,0)
    x = k % n
    y = n - 1
elif n_dir == 2: #(n-1,n - (k % n) -1)
    x = n - 1
    y = n - (k % n) -1
elif n_dir == 3: #(n - (k % n) -1,0)
    x = n - (k % n) -1
    y = 0

#거울에 반사되는 횟수 구하기
cnt = 0

#거울에 반사될 때, 바뀌는 화살표의 방향
#배열의 범위 밖이라면 종료
while(in_range(x,y)): 
    cnt += 1 

    #거울에 반사될 때, 바뀌는 화살표의 방향
    if mirrors[x][y] == '\\': # 0 <-> 3 / 1 <-> 2
        n_dir = 3 - n_dir

    elif mirrors[x][y] == '/':
        # 비트연산자로도 구현할 수 있다. n_dir = n_dir ^ 1
        # 가장 낮은 비트를 반전시키는 연산임
        if n_dir == 2 or n_dir == 3:
            n_dir = 5 - n_dir
        elif n_dir == 0 or n_dir == 1:
            n_dir = 1 - n_dir
    
    # 레이저의 위치를 변경한다.    
    x += mov_r[n_dir]
    y += mov_c[n_dir]

print(cnt)