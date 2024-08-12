# 위치에 따른 인덱스
direction = {
    'N':0,
    'W':1,
    'S':2,
    'E':3
}

mov_x = [0,-1,0,1]
mov_y = [1,0,-1,0]

# 현재 위치, 방향
x,y = 0,0
now_d = 0

ques = input()

ans = -1

# 입력받은 문자열을 순회하며 위치 이동
for t,mov in enumerate(ques):
    time = t+1

    # 왼쪽으로 90도 회전
    if mov == 'L':
        now_d = (now_d+1) % 4
    # 오른쪽으로 90도 회전
    elif mov == 'R':
        now_d = (now_d-1+4) % 4
    # 현재 방향으로 움직이기 
    else : # 'F' 일 때
        x += mov_x[now_d]
        y += mov_y[now_d]

    # x,y가 0으로 돌아왔을 때 break
    if x == 0 and y == 0:
        ans = time
        break
    
print(ans)