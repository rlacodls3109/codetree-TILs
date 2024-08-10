n = int(input())

# E,W,S,N 순으로 
dx, dy = [1,-1,0,0],[0,0,-1,1]

# 인덱스를 통해 dx, dy에 접근
Direction = ['E', 'W', 'S', 'N']
#초기 위치 설정
x, y = 0,0

for _ in range(n):
    D, a = tuple(input().split())
    a = int(a)
    # 주어진 문자에 대한 인덱스 탐색
    i = Direction.index(D)
    # 이동
    x += (dx[i]*a)
    y += (dy[i]*a)

print(x,y)