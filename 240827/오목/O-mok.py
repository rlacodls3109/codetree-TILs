import sys
arr = [
    list(map(int,input().split()))
    for _ in range(19)
]

def in_range(x,y):
    return x >= 0 and x < 19 and y >= 0 and y < 19 

'''
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

dxs = [0,1,1,1,0,-1,-1,-1]
dys = [1,1,0,-1,-1,-1,0,1]

for i in range(19):
    for j in range(19):

        if arr[i][j] != 0:
            for dx,dy in zip(dxs,dys):
                curt = 1
                curx = i
                cury = j

                while(1):
                    nx = curx + dx
                    ny = cury + dy

                    if in_range(nx,ny) and arr[nx][ny] == arr[i][j]:
                        curt += 1
                        curx = nx
                        cury = ny
                    else:
                        break
                    
                if curt == 5:
                    print(arr[i][j])
                    print(i + 2 * dx + 1, j + 2 * dy + 1)
                    sys.exit()

print(0)