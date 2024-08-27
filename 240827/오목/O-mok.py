import sys

# 바둑판 배열 입력
arr = [
    list(map(int,input().split()))
    for _ in range(19)
]

# 배열의 범위 내에 있는 지
def in_range(x,y):
    return x >= 0 and x < 19 and y >= 0 and y < 19 

'''
# 노가다 말고..진행 방향에 대한 배열 선언해서 풀기

def check_updown(x,y,color):
    if in_range(x-1,y) and in_range(x-2,y) and in_range(x+1,y) and in_range(x+2,y):
        return arr[x-1][y] == color and arr[x-2][y] == color and arr[x+1][y] == color and arr[x+2][y] == color

def check_side(x,y,color):
    if in_range(x,y-1) and in_range(x,y-2) and in_range(x,y+1) and in_range(x,y+2):
        return arr[x][y-1] == color and arr[x][y-2] == color and arr[x][y+1] == color and arr[x][y+2] == color

def check_Rdiagonal(x,y,color):
    if in_range(x-1,y-1) and in_range(x-2,y-2) and in_range(x+1,y+1) and in_range(x+2,y+2):
        return arr[x-1][y-1] == color and arr[x-2][y-2] == color and arr[x+1][y+1] == color and arr[x+2][y+2] == color

def check_Ldiagonal(x,y,color):
    if in_range(x-1,y+1) and in_range(x-2,y+2) and in_range(x+1,y-1) and in_range(x+2,y-2):
        return arr[x-1][y+1] == color and arr[x-2][y+2] == color and arr[x+1][y-1] == color and arr[x+2][y-2] == color

winner = 0 

for i in range(len(arr)):
    for j in range(len(arr[1])):
        if arr[i][j] != 0:
            color = arr[i][j]
            if check_side(i,j,color) or check_updown(i,j,color) or check_Rdiagonal(i,j,color) or check_Ldiagonal(i,j,color):
                winner = color
                winner_pos_x, winner_pos_y = i+1, j+1

if winner == 0:
    print(winner)
else :
    print(winner)
    print(winner_pos_x,winner_pos_y)

'''

#방향 이동을 위한 배열을 생성한다.
dxs = [0,1,1,1,0,-1,-1,-1]
dys = [1,1,0,-1,-1,-1,0,1]

for i in range(19):
    for j in range(19):

        # 0이면 돌이 놓여있지 않은 상태이므로 확인x
        if arr[i][j] != 0:
            # 모든 방향에 대해 검사한다.
            for dx,dy in zip(dxs,dys):
                curt = 1 #같은 돌이 나오는 횟수
                curx = i # 현재 x좌표
                cury = j # 현재 y좌표

                while(1):
                    #한칸 씩 이동
                    nx = curx + dx 
                    ny = cury + dy

                    #검사할 좌표가 배열의 범위 내에 있고, 같은 돌이라면
                    if in_range(nx,ny) and arr[nx][ny] == arr[i][j]:
                        curt += 1 
                        # 현 위치 좌표 변경
                        curx = nx 
                        cury = ny
                    # 아니라면 검사 종료
                    else:
                        break
                
                # 같은 돌이 5개 일 때 우승이다.
                if curt == 5:
                    print(arr[i][j])
                    print(i + 2 * dx + 1, j + 2 * dy + 1) # 가운데 좌표를 출력해야 함
                    
                    #프로그램 강제종료!
                    sys.exit()

print(0)