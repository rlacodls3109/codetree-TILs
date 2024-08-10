# 현 위치
now_dir = 3
x,y = 0,0

# E,S,W,N 순으로
dx, dy = [1,0,-1,0], [0,-1,0,1]

order = input()


for a in order:
    # 시계 반대방향으로 90도 회전
    if a == 'L':
        now_dir = (now_dir - 1 + 4) % 4
    
    # 시계방향으로 90도 회전
    elif a == 'R':
        now_dir = (now_dir + 1) % 4

    # 앞으로 한칸 이동
    else :
        x,y = x+dx[now_dir], y + dy[now_dir]

print(x, y)